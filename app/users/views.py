from sqlalchemy.orm.exc import NoResultFound

from flask import Blueprint, jsonify
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import login_required
from flask.ext.login import current_user

from .models import User

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/login', methods=['GET'])
def auth_login():
    email = 'vansanblch@gmail.com'

    try:
        user = User.query.filter_by(email = email).one()
        email = user.email
    except NoResultFound:
        email = None
        logout_user()

    if email:
        login_user(user)

    return jsonify({'email': email})


@mod.route('/logout', methods=['GET'])
@login_required
def auth_logout():
    logout_user()
    return jsonify({'email': None})


@mod.route('/email')
def auth_email():
    email = None

    if current_user.is_authenticated():
        email = current_user.email

    return jsonify({'email': email})
