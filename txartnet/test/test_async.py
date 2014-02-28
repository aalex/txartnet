# Copyright (c) 2014 Alexandre Quessy
# See LICENSE for details.

"""
Tests for txartnet/async.py

Maintainer: Alexandre Quessy
"""

from twisted.trial import unittest
from twisted.internet import reactor, defer, task
from txartnet import async

class TestEmpty(unittest.TestCase):
    """
    Empty test
    """
    def test_empty(self):
        self.failUnless(True)
