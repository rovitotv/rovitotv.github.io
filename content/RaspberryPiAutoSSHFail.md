Title: Securing Raspberry Pi SSH with Auto SSH Fail
Date: 2017-04-02 12:00
Modified: 2017-04-02 12:00
Category: Computing
Authors: Todd V. Rovito
Summary: Secure SSH on a Raspberry Pi with this simple Python script

My Raspberry Pi is used as a web server but I also use it to develop
Python code via SSH. My primary terminal into my Raspberry Pi is a
iPad Pro. I find the combination of a Raspberry Pi along with an 
iPad Pro a powerful combination.  It infuriates me when I look at 
/var/log/auth.log on my Raspberry Pi and see all the failed password
attempts. Use the command to find all of the failed password attempts:

```bash
cat /var/log/auth.log | grep 'Failed password'
```

Some of these crackers are repeatedly trying to crack
into my Raspberry Pi, with enough guesses they will eventually get in. 
To make matters worse they are trying popular user names such as 
"root", "admin", "php", etc.  None of these are valid accounts on my
Raspberry Pi but I need to find a way to stop these attempts.  This is
not my first rodeo so to speak I have been putting computers on the
internet since 1988.  For as long as I can remember Unix has had this
simple concept of /etc/hosts.allow and /etc/hosts.deny.  Simply put a
IP address in /etc/hosts.deny with the syntax "ALL: 2.60.223.100" and 
they won't even connect to the SSH daemon. The /etc/hosts.deny file
prevents these crackers from having infinite attempts to crack my 
Raspberry Pi and it reduces the load on the little computer because
any network traffic from a IP address in /etc/hosts.deny won't be
allowed to connect to sshd.  But the idea of manually going through
the /var/log/auth.log file and adding addresses to /etc/hosts.deny
sounds painful and not something I am likely to keep up with.  This 
is a perfect use case for a simple Python script.  So here is a 
Python script I wrote called auto_ssh_fail.py:

```python
# very simple program that scans /var/log/auth.log and looks for mis-behaving
# hosts.  Those mis-behaving hosts are then added to /etc/hosts.deny. This
# script is designed/tested on Raspbian Jesse.
#
import os

def read_secure_log():
	'''
		reads the file /var/log/auth.log
	'''
	with open('/var/log/auth.log', 'r') as secure_file:
		log_lines = secure_file.readlines()

	return log_lines

def get_ip_address(log_string):
	'''
		finds the ip address from the log string then returns it
	'''
	from_index = log_string.find("from ")
	if from_index > -1:
		log_string_split = log_string[from_index:-1].split(" ")
		if len(log_string_split) > 1:
			return log_string_split[1]
		else:
			return "NULL"

def parse_secure_log(secure_log_lines):
	'''
		parses the secure log lines looking for string 'Failed password'
	'''
	fail_ip_list = []
	for secure_index in range(0, len(secure_log_lines)):
		ban_ip = False
		if "Failed password" in secure_log_lines[secure_index]:
			if "invalid user" in secure_log_lines[secure_index]:
				ban_ip = True
			if "for root" in secure_log_lines[secure_index]:
				ban_ip = True
			if "for mail" in secure_log_lines[secure_index]:
				ban_ip = True

		if ban_ip:
			ip_address_to_ban = get_ip_address(secure_log_lines[secure_index])
			if ip_address_to_ban != "NULL":
				fail_ip_list.append(ip_address_to_ban)

	fail_ip_list.sort()
	fail_ip_set = set(fail_ip_list)
	fail_ip_list = list(fail_ip_set)
	return fail_ip_list

def add_hosts_to_deny(fail_ip_list):
	'''
		add hosts in fail_ip_list to hosts.deny checking to make sure it
		does not already exist
	'''
	ip_not_deined_list = []
	with open('/etc/hosts.deny', 'r') as hosts_deny_file:
		hosts_deny_lines = hosts_deny_file.readlines()

	# make sure fail_ip adress it not already in hosts.deny
	for fail_ip_index in range(0, len(fail_ip_list)):
		ip_not_denied = True
		for hosts_deny_index in range(0, len(hosts_deny_lines)):
			if fail_ip_list[fail_ip_index] in hosts_deny_lines[hosts_deny_index]:
				ip_not_denied = False
				break

		if ip_not_denied:
			ip_not_deined_list.append(fail_ip_list[fail_ip_index])

	# add ip_not_deined_list to hosts_deny
	for ip_not_deined_index in range(0, len(ip_not_deined_list)):
		hosts_deny_lines.append("ALL: %s\n" % ip_not_deined_list[ip_not_deined_index])

	# now write out new /etc/hosts.deny file
	with open('/etc/hosts.deny', 'w') as hosts_deny_file:
		hosts_deny_file.writelines(hosts_deny_lines)

if __name__ == "__main__":
	secure_log_lines = read_secure_log()
	fail_ip_list = parse_secure_log(secure_log_lines)
	print("detected %d mis-behaving ips" % len(fail_ip_list))
	print("following hosts will be deined")
	for i in range(0, len(fail_ip_list)):
		print(fail_ip_list[i])
	add_hosts_to_deny(fail_ip_list)

```

The script above is simple, feel free to edit for your needs.
Be careful that you don't lock out your own IP address by logging in
with the wrong password.  To install this script create a directory 
with the command:

```bash
mkdir /home/pi/auto_ssh_fail
```

Then copy the script above to /home/pi/auto_ssh_fail/auto_ssh_fail.py.
At this point you can run the script but it has to be run as root
because it will modify the file /etc/hosts.deny, so prepend the run 
command with sudo:

```bash
sudo python /home/pi/auto_ssh_fail/auto_ssh_fail.py
```

Then if you cat /etc/hosts.deny you should see IP addresses that 
correspond with failed password attempts in /var/log/auth.log:

```bash
cat /etc/hosts.deny
```
Now that you have the Python script auto_ssh_fail.py running we
need to have it run repeatedly automatically.  On Unix to run
programs automatically we use a tool called cron.  Cron is usually
installed in a system configuration in /etc/cron.hourly or 
/etc/cron.daily.  Scripts placed in /etc/cron.hourly are run
automatically every hour and scripts placed in /etc/cron.daily are
run once a day.  Raspbian is based on Debian which has this 
[bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=308911)
that scripts with certain file names will be ignored.  It took
me several hours to figure out why my script was not running on
the hour, it was called auto_ssh_fail.sh.  Apparently the ".sh"
at the end of the file name was ignored by the run-parts command
which is used by cron to execute scripts.  Care needs to be
taken that full paths are used in cron based scripts because
the full environment is not loaded. In /etc/cron.hourly or
/etc/cron.daily copy the following script:

```bash
#!/bin/sh

# run this script every hour to scan the /var/log/auth.log looking for
# mis-behaving ip addresses then add the ip address to hosts.deny

# Action!
echo "starting the auto_ssh_fail.py script ===========================================" >> /home/pi/auto_ssh_fail/auto_ssh_fail.log 2>&1
/bin/date >> /home/pi/auto_ssh_fail/auto_ssh_fail.log 2>&1
/usr/bin/python2.7 /home/pi/auto_ssh_fail/auto_ssh_fail.py >> /home/pi/auto_ssh_fail/auto_ssh_fail.log 2>&1
/bin/date >> /home/pi/auto_ssh_fail/auto_ssh_fail.log 2>&1
echo "finished the auto_ssh_fail.py script ===========================================" >> /home/pi/auto_ssh_fail/auto_ssh_fail.log 2>&1
```

Now every hour or once a day (I recommend once an hour) the 
log file /var/log/auth.log will be automatically scanned and
failed password attempts will be added to /etc/hosts.deny.  If
you run the script hourly then at most a cracker will have 60
minutes to attempt a break-in which is very difficult if you
use a strong password.  Another suggestion is to not use passwords
but 
[SSH keys](http://raspi.tv/2012/how-to-set-up-keys-and-disable-password-login-for-ssh-on-your-raspberry-pi).  SSH keys are long and are random, if you are
careful to protect your private key your Raspberry Pi would be
extremely difficult to crack.  