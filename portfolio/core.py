# -*- coding: utf-8 -*-

from flask.ext.login import LoginManager

from .services import users


lm = LoginManager()

@lm.user_loader
def load_user(userid):
    return users.get(userid)
