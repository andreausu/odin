# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from odin import create_app


class TestConfig:
    def test_dev_config(self):
        app = create_app('odin.settings.DevConfig')

        assert app.config['DEBUG'] is True

    def test_test_config(self):
        app = create_app('odin.settings.TestConfig')

        assert app.config['DEBUG'] is True
        assert app.config['WTF_CSRF_ENABLED'] is False

    def test_prod_config(self):
        app = create_app('odin.settings.ProdConfig')

        assert app.config['DEBUG'] is False
