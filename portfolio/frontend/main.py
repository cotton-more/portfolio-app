# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template


bp = Blueprint('frontend', __name__)


@bp.route('/')
def index():
    """index page"""
    return render_template('index.html')


@bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
