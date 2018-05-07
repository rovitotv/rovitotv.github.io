Title: Trying out OS X Fuse and SSHFS connected to Raspberry Pi
Date: 2016-02-06 23:53
Modified: 2016-02-06 23:53
Category: Computing
Authors: Todd V. Rovito
Summary: Experiments with OS X Fuse and SSHFS connected to Raspberry Pi

I am always seeking ways to improve my workflow.  As a heavy Sublime Text user I
had a colleague suggest [wbond Sublime
SFTP](https://wbond.net/sublime_packages/sftp/usage) but I just can't spend the
$30 for it.  Yes it is true I am cheap and I prefer open source software, it is
bad enough I had to buy Sublime Text because I was using it so much.  Another
alternative that I wanted to investigate was
[SSHFS](https://en.wikipedia.org/wiki/SSHFS).  SSHFS lets a user "mount" a
remote file system with no additional software on the server side except for
standard ssh.  After the remote file system is mounted Sublime Text can be
used to edit files or do any other standard file command from the shell as
if the file system were local.

This is a little confusing but SSHFS is designed to use [FUSE which stands for
Filesystem In Userspace](https://en.wikipedia.org/wiki/Filesystem_in_Userspace).
FUSE basically allows non-privileged users create their own file systems
without messing with the kernel.  I have heard of people using it to access
NTFS hard disks in the past as well.  SSHFS is a "plugin" for FUSE.

So what do you have to install on OS X to get this to work. First off I am
running on 10.11.3 OS X El Capitan the latest at the time of writing this post.

1. Install [OS X Fuse](http://osxfuse.github.io) they have a nice installer
of the stable release.  For added flexibility I would install the Mac Fuse
compatibility layer as you will be able to support more file systems.  This
is not needed if you just want to use SSHFS.
2. Install [SSHFS](http://osxfuse.github.io) they have a nice installer of the
stable release.
3. A reboot is recommended.
4. To mount a file system you use the command "sshfs" from the OS X terminal
which is similar to the standard mount command:
```bash
sshfs pi@192.168.1.9:/ ~/temp/pi/
```
Then if you perform a `df -h` command you will notice that a new file system
is mounted.
```bash
Todds-MacBook-Pro:pi rovitotv$ df -h
Filesystem         Size   Used  Avail Capacity   iused     ifree %iused  Mounted on
/dev/disk1        1.8Ti  810Gi  1.0Ti    44% 212471929 275606053   44%   /
devfs             193Ki  193Ki    0Bi   100%       666         0  100%   /dev
map -hosts          0Bi    0Bi    0Bi   100%         0         0  100%   /net
map auto_home       0Bi    0Bi    0Bi   100%         0         0  100%   /home
pi@192.168.1.9:/   13Gi  4.2Gi  8.5Gi    33%    144854    752746   16%   /Users/rovitotv/temp/pi
```
Once a remote file system is mounted you can use the finder or the terminal
as normal and all commands that occur from /Users/rovitotv/temp/pi happen
on the Raspberry Pi.  Performance seems to be decent even over wi-fi.


After all your work is completed you can unmount the volume with the command:

```bash
umount /Users/rovitotv/temp/pi
```


