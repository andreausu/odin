# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from flask import Blueprint, request, render_template

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.jinja')
