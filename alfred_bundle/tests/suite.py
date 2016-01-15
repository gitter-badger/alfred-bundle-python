#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

import unittest

from .test_utils import TestUtils


class TestSuite(object):

    def __init__(self):
        self.suite = unittest.TestSuite()
        self.cases = (
            TestUtils(),
        )
        self.suite.addTests(self.cases)
        self.runner = unittest.TextTestRunner()

    def run(self):
        return self.runner.run(self.suite)
