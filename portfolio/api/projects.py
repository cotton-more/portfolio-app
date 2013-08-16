# -*- coding: utf-8 -*-

from flask import Blueprint

from portfolio.services import projects
from portfolio.services import cards
from . import route


bp = Blueprint('projects', __name__, url_prefix='/projects')


@route(bp, '/')
def list():
    return projects.all()


@route(bp, '/<project_id>/cards')
def show_cards(project_id):
    return cards.find(parent_id=project_id).all()


@route(bp, '/<project_id>')
def show(project_id):
    return projects.get_or_404(project_id)
