# -*- coding: utf-8 -*-

from flask.ext.login import UserMixin

from .. import db
from .. import JsonSerializer


class UserJsonSerializer(JsonSerializer):
    __json_public__ = ['id', 'email']


class User(UserJsonSerializer, UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    role = db.Column(db.String(128))

    def __repr__(self):
        return "<User(%s, %s)>" % (self.email, self.role)
