#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Sean Herron'
SITENAME = u'openNASA'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

DEFAULT_DATE = "fs"

DEFAULT_PAGINATION = False

TYPOGRIFY = True

THEME = "themes/opennasa"

ARTICLE_URL = '{slug}'

READERS = {'html': None}

PATH = 'content'
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATH = 'plugins'
PLUGINS = ['gravatar']