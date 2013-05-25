from flask import Blueprint, jsonify, session, abort, request

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/login')
def auth_login():
    assertion = request.args.get('assertion', False)
    if False == assertion:
        abort(400)

    import requests
    assertion_info = {'assertion': assertion,
                        'audience': '127.0.0.1:5000' } # window.location.host
    resp = requests.post('https://verifier.login.persona.org/verify',
                        data=assertion_info, verify=True)

    if not resp.ok:
        abort(500)

    data = resp.json()

    if data['status'] == 'okay':
        session.update({'email': data['email']})

    return jsonify(data)

@mod.route('/logout')
def auth_logout():
    session.pop('email', None)
    email = session.get('email', None)

    return jsonify({'email': email})

@mod.route('/email')
def auth_email():
    email = session.get('email', None)

    return jsonify({'email': email})
