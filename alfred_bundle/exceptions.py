#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Ritashugisha
# MIT License. <http://opensource.org/licenses/MIT>


class AlfredBundleException(Exception):
    _code = 7000

    def __init__(self):
        super(AlfredBundleException, self).__init__(message)
        self.code = (code if code else self._code)


class WorkflowException(AlfredBundleException):
    _code = 7100


class InvalidWorkflowException(WorkflowException):
    _code = 7110


class MissingInfoPlistException(InvalidWorkflowException):
    _code = 7111


class InvalidInfoPlistException(InvalidWorkflowException):
    _code = 7112
