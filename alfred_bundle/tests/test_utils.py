#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

import os
import tempfile
import unittest

from .. import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def runTest(self):
        self.test_file_contains_data()

    def test_file_contains_data(self):
        test_file = tempfile.mkstemp()[-1]
        self.assertFalse(utils.file_contains_data(test_file))
        with open(test_file, 'w') as f:
            f.write('test')
        self.assertTrue(utils.file_contains_data(test_file))
        os.remove(test_file)
        self.assertFalse(utils.file_contains_data(test_file))
