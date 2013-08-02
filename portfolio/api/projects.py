# -*- coding: utf-8 -*-

from flask import Blueprint

from portfolio.services import projects
from . import route


bp = Blueprint('projects', __name__, url_prefix='/projects')


@route(bp, '/')
def list():
    return projects.all()


@route(bp, '/<project_id>')
def show(project_id):
    return projects.get_or_404(project_id)
