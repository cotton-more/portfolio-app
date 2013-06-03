from flask import Blueprint, jsonify, render_template

from app.portfolio.models import Project, Card

mod = Blueprint('portfolio', __name__,
                url_prefix='/portfolio',
                template_folder='templates')

@mod.route('/projects')
def menu_list():
    result = [e.json() for e in Project.query.all()]

    return jsonify(result=result)


@mod.route('/get_cards/<int:project_id>')
def get_cards(project_id):
    q = Card.query.filter(Card.project_id==project_id)
    cards = [e.json() for e in q.all()]

    return jsonify(result=cards)


@mod.route('/', defaults={'path': ''})
@mod.route('/<path:path>')
def index(path):
    return render_template('portfolio.html')
