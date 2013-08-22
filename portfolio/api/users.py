# -*- coding: utf-8 -*-

from flask import Blueprint, request
from flask.ext.login import login_required, logout_user, login_user

from . import route
from ..services import users

bp = Blueprint('users', __name__, url_prefix='/users')


@route(bp, '/login', methods=['GET', 'POST'])
def login():
    email = None
    # email = 'vansanblch@gmail.com'

    if request.json is not None:
        email = request.data['email']

    user = users.find(email=email).first()
    if email and user:
        login_user(user)
    else:
        email = None

    return {'email': email}


@route(bp, '/logout')
@login_required
def logout():
    logout_user()

    return {'email': None}


@route(bp, '/email')
def auth_email():
    email = None

    return {'email': email}
