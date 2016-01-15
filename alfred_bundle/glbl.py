#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>


import os
import sys
import logging

from datetime import datetime

# Module information
MODULE_NAME = 'Alfred Bundle'
MODULE_DOC = '''{module} is A specialized port of the Alfred Bundler project for Python.
For more information about {module} read the documentation.'''.format(
    module=MODULE_NAME
)

# Versioning information, as standardized by Semantic Versioning 2.0.0
# See <http://semver.org/> for more information
VERSIONING = (
    'devel',
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
    'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces',
)
VERSION_DATA = {'major': 0, 'minor': 0, 'revision': '0'}
VERSION_DATA['release'] = VERSIONING[VERSION_DATA['major']]
VERSION_NUMBER = '{major}.{minor}.{revision}'.format(**VERSION_DATA)
VERSION = '{release}.{major}.{minor}r{revision}'.format(**VERSION_DATA)

# Module package information
PACKAGE = '{module}<{version}>'.format(module=MODULE_NAME, version=VERSION)

# Module author information, required some form of name and contact for backlog
AUTHOR_DATA = (
    {'name': 'Ritashugisha', 'contact': 'ritashugisha@gmail.com'},
)
AUTHOR = '\n'.join(['{name} ({contact})'.format(**_) for _ in AUTHOR_DATA])
TEAM_DATA = {
    'name': '{module} Team'.format(module=MODULE_NAME),
    'count': len(AUTHOR_DATA)
}
TEAM = '{name} ({count} members)'.format(**TEAM_DATA)

# Copyright information, MIT License <http://opensource.org/licenses/MIT>
COPYRIGHT_DATA = {'year': datetime.now().year, 'holders': TEAM}
COPYRIGHT = 'Copyright (c) {year} {holders}'.format(**COPYRIGHT_DATA)
LICENSE = '''The MIT License (MIT)
{copyright}
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.'''.format(copyright=COPYRIGHT)

# Module framework variables
FROZEN = hasattr(sys, 'frozen')
DIRECTORY_PERMISSIONS = 0775

# Static module framework paths
BASE_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PARENT_DIR = os.path.dirname(BASE_DIR)
HOME_DIR = os.path.expanduser('~')
SUPPORT_DIR = os.path.join(HOME_DIR, 'Library', 'Application Support')
CACHE_DIR = os.path.join(HOME_DIR, 'Library', 'Caches')

# Alfred specific paths
ALFRED_NAME = 'Alfred 2'
ALFRED_ID = 'com.runningwithcrayons.Alfred-2'
ALFRED_PREFS_NAME = 'Alfred.alfredpreferences'
ALFRED_SUPPORT_DIR = os.path.join(SUPPORT_DIR, ALFRED_NAME)
ALFRED_WORKFLOW_DIR = os.path.join(ALFRED_SUPPORT_DIR, 'Workflow Data')
ALFRED_LICENSE_PATH = os.path.join(ALFRED_SUPPORT_DIR, 'license.plist')
ALFRED_USAGE_PATH = os.path.join(ALFRED_SUPPORT_DIR, 'usage.data')
ALFRED_DATABASE_DIR = os.path.join(ALFRED_SUPPORT_DIR, 'Databases')
ALFRED_PREFS_PATH = os.path.join(ALFRED_SUPPORT_DIR, ALFRED_PREFS_NAME)
ALFRED_PREFERENCES_DIR = os.path.join(ALFRED_PREFS_PATH, 'preferences')
ALFRED_WORKFLOW_DIR = os.path.join(ALFRED_PREFS_PATH, 'workflows')
ALFRED_SNIPPETS_DATABASE_PATH = os.path.join(
    ALFRED_PREFS_PATH, 'clipboard', 'snippets.alfdb'
)
ALFRED_CACHE_DIR = os.path.join(CACHE_DIR, ALFRED_ID)
ALFRED_CACHE_DATABASE_PATH = os.path.join(ALFRED_CACHE_DIR, 'Cache.db')
ALFRED_WORKFLOW_CACHE_DIR = os.path.join(ALFRED_CACHE_DIR, 'Workflow Data')

# Bootstrap variables
BOOTSTRAPPED = False

# Module logging
LOGGING_LVL = logging.DEBUG
LOGGING_FMT = (
    '[%(asctime)s] [%(levelname)-8s] '
    '[%(filename)s@%(funcName)s:%(lineno)s] %(message)s'
)
logging.basicConfig(level=LOGGING_LVL, format=LOGGING_FMT)
LOG = logging.getLogger(MODULE_NAME)
