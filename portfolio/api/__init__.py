# -*- coding: utf-8 -*-

from flask import jsonify

from .. import factory
from .. import JSONEncoder


def create_app(settings_override=None, register_security_blueprint=False):
    """Returns the Overholt API application instance"""

    app = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=register_security_blueprint)

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    # Register custom error handlers
    #app.errorhandler(OverholtError)(on_overholt_error)
    #app.errorhandler(OverholtFormError)(on_overholt_form_error)
    app.errorhandler(404)(on_404)

    return app


def on_404(e):
    return jsonify(dict(error='Not found')), 404
