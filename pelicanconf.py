#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Todd V. Rovito'
SITENAME = "rovitotv's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Raspberry Pi', 'https://www.raspberrypi.org'),
         ('AFRL', 'http://teamafrl.afciviliancareers.com'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/rovitotv'),
          ('GitHub', 'https://github.com/rovitotv'),
          ('YouTube', 'https://www.youtube.com/channel/UCBl6ggrOjOtyoyXsdNvKouA'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['MediaFiles']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  

PLUGINS = [
    # ...
    'pelican_youtube',
    # ...
]
