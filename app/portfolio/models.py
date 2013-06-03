from app import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    tags = db.Column(db.String(255))

    cards = db.relationship("Card",
                          backref="menu"
                          )

    def json(self):
        """Turn entity into json-ready object"""

        project = {
            'id': self.id,
            'name': self.name,
            'about': self.about,
            'tags': self.tags,
            'cards_len': len(self.cards)
        }

        if (project['tags']):
            project['tags'] = [ tag.strip() for tag in self.tags.split(',') ]

        return project

    def __repr__(self):
        return "<Project(%s, %s)>" % (self.id, self.name)


class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    name = db.Column(db.String(128))
    about = db.Column(db.Text)
    image = db.Column(db.String(128))

    def json(self):
        """Turn entity into json-ready object"""
        return {
            'id': self.id,
            'menu_id': self.menu_id,
            'name': self.name,
            'about': self.about,
            'image': self.image
        }

    def __repr__(self):
        return "<Card(%d, %s)>" % (self.id, self.name)


