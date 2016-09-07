# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""

from odin import db
from odin.models.base import Base
from odin.models.meeting import Meeting


class Person(Base):
    """Person Model"""
    __tablename__ = 'people'
    first_name = db.Column(db.Text())
    last_name = db.Column(db.Text())
    location = db.Column(db.Text())
    start_date = db.Column(db.DateTime())
    bio = db.Column(db.Text())

    goals = db.relationship(
        'PersonGoal', backref='person',
        lazy='dynamic', cascade='all, delete-orphan'
    )
    meetings = db.relationship(
        'Meeting', backref='person',
        lazy='dynamic', cascade='all, delete-orphan'
    )


class PersonGoal(Base):
    """Goals of a Person"""
    __tablename__ = 'people_goals'
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    goal = db.Column(db.Text())
