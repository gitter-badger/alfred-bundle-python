#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

import os


def file_contains_data(filepath):
    """ Ensures the given `filepath` exists and has data stored.

    :param filepath: The real path to the file in question
    :type filepath: str
    :rtype: bool

    """
    return os.path.isfile(filepath) and os.stat(filepath).st_size > 0
