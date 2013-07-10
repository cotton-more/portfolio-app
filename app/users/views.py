from flask import Blueprint, jsonify, session

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/login', methods=['POST'])
def auth_login():

    data = {'email': 'test@example.com'}

    return jsonify(data)

@mod.route('/logout', methods=['POST'])
def auth_logout():
    session.pop('email', None)
    email = session.get('email', None)

    return jsonify({'email': email})

@mod.route('/email')
def auth_email():
    email = session.get('email', None)

    return jsonify({'email': email})
