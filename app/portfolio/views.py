import json

from flask import request
from flask import Blueprint
from flask import Response
from flask import render_template
from flask import url_for
from sqlalchemy.orm import joinedload

from app.portfolio.models import Portfolio
#from app.portfolio.models import Card
from app.portfolio.models import Project

mod = Blueprint('portfolio', __name__,
                url_prefix='/portfolio',
                template_folder='templates')


@mod.route('/projects/save', methods=["POST"])
def save():
    data = json.loads(request.data)
    entity = Portfolio.query.get(int(data['id']))

    return Response(json.dumps(entity), mimetype='application/json')


@mod.route('/projects')
def projects():
    rows = Project.query.with_entities(Project.name, Project.id).all()

    result = []

    for e in rows:
        project = {
            "name": e.name,
            "url": url_for("portfolio.view_project", id=e.id)
        }
        result.append(project)

    return Response(json.dumps(result), mimetype='application/json')


@mod.route('/projects/<int:id>')
def view_project(id):
    e = Project.query.options(joinedload('cards')).filter(Project.id==id).one()

    result = e.json()
    result["id"] = e.id
    result["cards"] = [ card.json() for card in e.cards ]

    return Response(json.dumps(result), mimetype='application/json')


@mod.route('/', defaults={'path': ''})
@mod.route('/<path:path>')
def index(path):
    return render_template('portfolio.html')
