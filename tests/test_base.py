# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from flask_testing import TestCase

from odin import create_app as app, db


class BaseTestCase(TestCase):
    """A base test case for odin"""
    def create_app(self):
        test_app = app('odin.settings.TestConfig')
        return test_app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
