# -*- coding: utf-8 -*-

from functools import wraps

from portfolio import factory


def create_app(settings_override=None):
    """Returns the portfolio dashboard application instance"""

    app = factory.create_app(__name__, __path__, settings_override)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            pass
            # TODO
            #app.errorhandler(e)(handle_error)

    return app


def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        #@login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
