# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""

import os

_cwd = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    SECRET_KEY = 'secret'
    LOG_FILE = os.path.join(_cwd, 'odin.log')


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True


class TestConfing(Config):
    ENV = 'test'
    DEBUG = True
    WTF_CSRF_ENABLED = False
