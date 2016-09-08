# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from flask import url_for

from tests.test_base import BaseTestCase


class MainViewTests(BaseTestCase):
    def test_home_page_loads(self):
        response = self.client.get(url_for('main.home'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue("feedback" in response.get_data(as_text=True))
