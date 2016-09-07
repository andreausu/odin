#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""

import os
import sys

from flask_script import Manager, Server

from odin import create_app

env = os.environ.get('ODIN_ENV', 'dev')
app = create_app('odin.settings.{0}Config'.format(env.capitalize()))

manager = Manager(app)
manager.add_command("server", Server)


if __name__ == "__main__":
    manager.run()
