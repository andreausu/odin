# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from odin import db
from odin.models.base import Base


class Meeting(Base):
    """Meeting Model"""
    __tablename__ = 'meetings'
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    start_date = db.Column(db.DateTime())
    bio = db.Column(db.Text())

    action_items = db.relationship(
        'MeetingActionItem', backref='meeting',
        lazy='dynamic', cascade='all, delete-orphan'
    )


class MeetingActionItem(Base):
    """Meeting Action Item Model"""
    __tablename__ = 'meeting_action_items'
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'))
    status_id = db.Column(
        db.Integer, db.ForeignKey('meeting_action_item_status.id'))
    priority_id = db.Column(
        db.Integer, db.ForeignKey('meeting_action_item_priority.id'))
    description = db.Column(db.Text())
    due_date = db.Column(db.DateTime())
    completed_date = db.Column(db.DateTime())

    statuses = db.relationship(
        'MeetingActionItemStatus', backref='MeetingActionItem',
        lazy='dynamic'
    )
    priorities = db.relationship(
        'MeetingActionItemPriorty', backref='MeetingActionItem',
        lazy='dynamic'
    )


class MeetingActionItemStatus(Base):
    __tablename__ = 'meeting_action_item_status'
    status = db.Column(db.Text())


class MeetingActionItemPriorty(Base):
    __tablename__ = 'meeting_action_item_priority'
    priority = db.Column(db.Integer)
