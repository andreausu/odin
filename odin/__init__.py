# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from flask import Flask

from odin.controllers.main.views import main
from odin.extensions import (
    bootstrap,
    db
)


def create_app(object_name):
    """
    Flask Application Factory
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: Python path of the config object
    """
    app = Flask(__name__)

    app.config.from_object(object_name)

    # Initialize Extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(main)

    return app
