import json

from flask import Blueprint
from flask import Response
from flask import render_template

from app.portfolio.models import Portfolio
from app.portfolio.models import Card
from app.portfolio.models import Project

mod = Blueprint('portfolio', __name__,
                url_prefix='/portfolio',
                template_folder='templates')


@mod.route('/<int:id>/save', methods=["POST"])
def save(id):
    entity = Portfolio.query.get(id)

    return Response(json.dumps(entity), mimetype='application/json')


@mod.route('/projects')
def menu_list():
    result = [e.json() for e in Project.query.all()]

    return Response(json.dumps(result), mimetype='application/json')


@mod.route('/<int:project_id>/cards')
def get_cards(project_id):
    q = Card.query.filter(Card.parent_id==project_id)
    result = [e.json() for e in q.all()]

    return Response(json.dumps(result), mimetype='application/json')


@mod.route('/', defaults={'path': ''})
@mod.route('/<path:path>')
def index(path):
    return render_template('portfolio.html')
