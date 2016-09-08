# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from datetime import datetime

from tests.test_base import BaseTestCase

from odin import db
from odin.models.person import Person, PersonGoal


class TestModelPerson(BaseTestCase):

    def test_person_in_session(self):
        p = Person()
        db.session.add(p)
        db.session.commit()

        assert p in db.session

    def test_can_add_new_person(self):
        p = Person(
            first_name='Lev',
            last_name='Lazinskiy',
            location='San Francisco',
            start_date=datetime.utcnow(),
            bio='Having the best day of hist life!'
        )
        db.session.add(p)
        db.session.commit()

        people = Person.query.all()

        assert len(people) == 1

        lev = Person.query.filter_by(first_name='Lev').first()

        assert lev.location == 'San Francisco'

        noone = Person.query.filter_by(first_name='No One').all()

        assert len(noone) == 0
