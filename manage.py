#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""

import os
import sys
import unittest
import xmlrunner

from flask_script import Manager, Server
from flask_script.commands import Command
from flask_migrate import Migrate, MigrateCommand

from odin import create_app, db
from odin.models.person import Person, PersonGoal
from odin.models.meeting import Meeting, MeetingActionItem, \
    MeetingActionItemStatus, MeetingActionItemPriorty


class Test(Command):
    def run(self):
        tests = unittest.TestLoader().discover('tests')
        results = xmlrunner.XMLTestRunner(output='test-reports').run(tests)


env = os.environ.get('ODIN_ENV', 'dev')
app = create_app('odin.settings.{0}Config'.format(env.capitalize()))

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)
manager.add_command('test', Test)


if __name__ == "__main__":
    manager.run()
