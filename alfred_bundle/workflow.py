#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

import os
import plistlib

from . import glbl
from . import utils
from . import exceptions


class Workflow(object):

    def __init__(self, info_plist):
        if os.path.exists(info_plist):
            if utils.file_contains_data(info_plist):
                self.plist_path = info_plist
                self.plist = plistlib.readPlist(self.plist_path)
                self.workflow_directory = os.path.dirname(self.plist_path)
            else:
                raise exceptions.InvalidInfoPlistException((
                    "invalid 'info.plist' at '{}'"
                ).format(info_plist))
        else:
            raise exceptions.MissingInfoPlistException((
                "missing 'info.plist' at '{}'"
            ).format(info_plist))

    def __repr__(self):
        return '<{} {}>'.format(
            self.__class__.__name__,
            self.id
        )

    @property
    def id(self):
        return self.plist.get('bundleid', None)

    @property
    def name(self):
        return self.plist.get('name', None)

    @property
    def description(self):
        return self.plist.get('description', None)

    @property
    def category(self):
        return self.plist.get('category', None)

    @property
    def author(self):
        return self.plist.get('createdby', None)

    @property
    def readme(self):
        return self.plist.get('readme', None)

    @property
    def url(self):
        return self.plist.get('webaddress', None)

    @property
    def disabled(self):
        return self.plist.get('disabled', None)

    @property
    def objects(self):
        return self.plist.get('objects', None)

    @property
    def connections(self):
        return self.plist.get('connections', None)

    @property
    def uidata(self):
        return self.plist.get('uidata', None)
