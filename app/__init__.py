from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('assets/favicon.ico')

from app.portfolio.views import mod as portfolioModule
app.register_blueprint(portfolioModule)

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.pages.views import mod as pagesModule
app.register_blueprint(pagesModule)
