#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>

import textwrap
import setuptools

VERSION = '0.1'


if __name__ == '__main__':
    setuptools.setup(
        name='Alfred Bundle',
        version=VERSION,
        description='Alfred Python utility bundle',
        author='Ritashugisha',
        author_email='ritashugisha@gmail.com',
        url='',
        long_description=textwrap.dedent("""
        """),
        packages=[
            'alfred_bundle',
            'alfred_bundle.tests'
        ],
        package_data={},
        classifiers=[],
        test_suite='alfred_bundle.tests.common',
        use_2to3=True
    )
