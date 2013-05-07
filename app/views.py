from app import app
#from models import User
from models import Menu
from models import Card
from flask import jsonify
from flask import request, current_app
from flask import abort, session

from functools import wraps

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs).data) + ')'
            return current_app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route('/menu/list')
@support_jsonp
def menu_list():
    menu = [e.json() for e in Menu.query.all()]

    return jsonify(result=menu)

@app.route('/get_cards/<int:menu_id>')
@support_jsonp
def get_cards(menu_id):
    q = Card.query.filter(Card.menu_id==menu_id)
    cards = [e.json() for e in q.all()]

    return jsonify(result=cards)

@app.route('/auth/login')
@support_jsonp
def auth_login():
    assertion = request.args.get('assertion', False)
    if False == assertion:
        abort(400)

    import requests
    assertion_info = {'assertion': assertion,
                        'audience': 'localhost:9000' } # window.location.host
    resp = requests.post('https://verifier.login.persona.org/verify',
                        data=assertion_info, verify=True)

    if not resp.ok:
        abort(500)

    data = resp.json()

    if data['status'] == 'okay':
        session.update({'email': data['email']})

    return jsonify(data)

@app.route('/auth/logout')
@support_jsonp
def auth_logout():
    session.pop('email', None)
    email = session.get('email', None)

    return jsonify({'email': email})

@app.route('/auth/email')
@support_jsonp
def auth_email():
    email = session.get('email', None)

    return jsonify({'email': email})
