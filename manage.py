#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""

import os
import sys

from flask_script import (
    Manager,
    Server
)
from flask_migrate import (
    Migrate,
    MigrateCommand
)

from odin import create_app, db
from odin.models.person import (
    Person,
    PersonGoal
)
from odin.models.meeting import (
    Meeting,
    MeetingActionItem,
    MeetingActionItemStatus,
    MeetingActionItemPriorty
)

env = os.environ.get('ODIN_ENV', 'dev')
app = create_app('odin.settings.{0}Config'.format(env.capitalize()))

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
