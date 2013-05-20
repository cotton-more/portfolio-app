from flask import Blueprint, jsonify

from app.portfolio.models import Menu, Card

mod = Blueprint('portfolio', __name__, url_prefix='/portfolio')

@mod.route('/menu/list')
def menu_list():
    menu = [e.json() for e in Menu.query.all()]

    return jsonify(result=menu)

@mod.route('/get_cards/<int:menu_id>')
def get_cards(menu_id):
    q = Card.query.filter(Card.menu_id==menu_id)
    cards = [e.json() for e in q.all()]

    return jsonify(result=cards)
