import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_ECHO = True

ADMIN_EMAIL = 'vansanblch@gmail.com'

SECRET_KEY = 'development key'
