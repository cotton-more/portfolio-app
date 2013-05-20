from flask.ext.login import UserMixin

from app import db
from app.users.constants import GUEST

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    role = db.Column(db.String(128), unique=True, default=GUEST)

    def __repr__(self):
        return "<User(%s, %s)>" % (self.email, self.role)
