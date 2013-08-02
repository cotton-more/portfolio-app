# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property

from .. import db
from .. import JsonSerializer


class Portfolio(db.Model):
    __tablename__ = 'portfolio'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    type = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_on': type
    }


class ProjectJsonSerializer(JsonSerializer):
    __json_modifiers__ = {
        'tags': lambda x, self: self.tags
    }
    __json_hidden__ = ['_tags']


class Project(ProjectJsonSerializer, Portfolio):
    __mapper_args__ = {
        'polymorphic_identity': 'project'
    }

    _tags = db.Column('tags', db.String(255))

    @hybrid_property
    def tags(self):
        if self._tags is None:
            return None
        else:
            return [ tag.strip() for tag in self._tags.split(',') ]

    @tags.setter
    def tags(self, value):
        if value:
            self._tags = ','.join(value)

    #def __repr__(self):
        #return "<Project(%s, %s)>" % (self.id, self.name)


class Card(JsonSerializer, Portfolio):
    __mapper_args__ = {
        'polymorphic_identity': 'card'
    }

    parent_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))
    image = db.Column(db.String(128))

    #project = db.relationship(Project, backref="cards", remote_side=Project.id)

    def __repr__(self):
        return "<Card(%d, %s)>" % (self.id, self.name)
