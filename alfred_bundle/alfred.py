#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

import os
import base64
import sqlite3
import plistlib

from . import glbl
from . import utils
from . import workflow
from . import exceptions


class Alfred(object):
    """ Alfred interaction and information class.

    """
    _name = glbl.ALFRED_NAME
    _id = glbl.ALFRED_ID
    _license = glbl.ALFRED_LICENSE_PATH
    _usage = glbl.ALFRED_USAGE_PATH
    _support = glbl.ALFRED_SUPPORT_DIR
    _cache = glbl.ALFRED_CACHE_DIR
    _workflow_data = glbl.ALFRED_WORKFLOW_DIR
    _workflow_cache = glbl.ALFRED_WORKFLOW_CACHE_DIR
    _databases = [
        os.path.join(glbl.ALFRED_DATABASE_DIR, i)
        for i in os.listdir(glbl.ALFRED_DATABASE_DIR)
    ] + [glbl.ALFRED_SNIPPETS_DATABASE_PATH, glbl.ALFRED_CACHE_DATABASE_PATH]
    _preferences = glbl.ALFRED_PREFS_PATH

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def support(self):
        return self._support

    @property
    def cache(self):
        return self._cache

    @property
    def workflow_data(self):
        return self._workflow_data

    @property
    def workflow_cache(self):
        return self._workflow_cache

    @property
    def license(self):
        if utils.file_contains_data(self._license):
            return plistlib.readPlist(open(self._license, 'r'))

    @property
    def usage(self):
        if utils.file_contains_data(self._usage):
            with open(self._usage, 'r') as f:
                return dict(zip(
                    ['time', 'usage', 'hash'],
                    base64.b64decode(f.read()).split('||')
                ))

    @property
    def databases(self):
        retn = {}
        for i in self._databases:
            if os.path.exists(i):
                key = os.path.splitext(os.path.basename(i))[0].lower()
                try:
                    retn[key] = sqlite3.connect(i)
                except sqlite3.OperationalError:
                    retn[key] = None
        return retn

    def get_preferences(self):
        retn = {'appearance': {}, 'features': {}, 'local': {}}
        preferences_path = os.path.join(self._preferences, 'preferences')

        for key in retn.keys():
            for (root, direc, files,) in \
                    os.walk(os.path.join(preferences_path, key)):
                for f in files:
                    if os.path.splitext(f)[1].lower() == '.plist':
                        retn[key][os.path.basename(root)] = \
                            plistlib.readPlist(os.path.join(root, f))

        return retn

    def get_workflows(self):
        retn = {}
        workflows_path = os.path.join(self._preferences, 'workflows')

        for i in os.listdir(workflows_path):
            try:
                retn[os.path.basename(i)] = workflow.Workflow(
                    os.path.join(workflows_path, i, 'info.plist')
                )
            except exceptions.InvalidWorkflowException:
                retn[os.path.basename(i)] = None

        return retn
