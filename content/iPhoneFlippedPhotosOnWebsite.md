Title: Photos from iPhone are flipped on Website
Date: 2018-01-27 22:57
Modified: 2018-01-27 22:57
Category: Computing
Authors: Todd V. Rovito
Summary: Photos taken with my iPhone were appearing upside down on my website

This has been a frustrating problem for several months with my Pelican
powered Raspberry Pi web server.  I actually thought maybe I was crazy 
because I would visit my website on my computer and everything looked
fine but then if I went to my website with iPhone/iPad some of the 
pictures were upside down.  I tried using Image Magick's convert 
command to rotate the images and that didn't fix the problem.  Finally
tonight I thought I would really dive in and focus trying to figure out
what was going on.  The first thing I tried was different Pelican themes,
maybe a responsive theme would fix my issue?  I could not get the other
themes to work so I started really looking at the images and the exif
data inside of the JPEG images.  After some searching around the web
I discovered that other people had this problem.  Basically if you
take photos with your iPhone with the volume buttons oriented up
that is really upside down.  Instead of rotating the images the iPhone
puts the information into the Exif headers of the JPEG image.  But then
it behaves differently for web browsers (both MacOS and Windows) and
iPhone/iPad.  On MacOS and Windows the images had to be rotated with
the convert and they displayed fine.  But then on iPhone/iPad they
would display upside down after the convert program was used to rotate
them.  Finally I was able to assemble a Python program to rotate the
image if orientation is set then to strip out all the exif data for
presentation on the web.  Here is the program:
```python
import argparse
from PIL import Image, ExifTags

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", action="store", required=True)
    args = parser.parse_args()

    print("processing file: %s" % args.filename)
    image = Image.open(args.filename)
    # this code below will rotate the image if it needs to be rotated
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation]=='Orientation':
            break
    exif=dict(image._getexif().items())

    if exif[orientation] == 3:
        image=image.rotate(180, expand=True)
        print("rotated image 180")
    elif exif[orientation] == 6:
        image=image.rotate(270, expand=True)
        print("rotated image 270")
    elif exif[orientation] == 8:
        image=image.rotate(90, expand=True)
        print("rotated image 90")

    # now we need to strip out the exif all together by saving
    # to a new image without exif
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(args.filename)
```

Then be careful that you clear your web cache so the same
upside down image does not reload.  Hopefully this will save
you some time!
