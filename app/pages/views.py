from flask import Blueprint, render_template

mod = Blueprint('pages', __name__, url_prefix="/")

@mod.route('/')
@mod.route('/index')
def index():
    return render_template('index.html')
