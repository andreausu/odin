# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
import pytest
from odin import create_app


@pytest.yield_fixture
def app():
    app = create_app('odin.settings.TestConfig')
    yield app


@pytest.yield_fixture
def app_client():
    client = app.test_client()
    yield client
