from setup_db import db
from marshmallow import Schema, fields
from dao.model.genre import Genre


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class UserFullSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    favorite_genre = fields.Method("get_favorite_genre", dump_only=True)

    def get_favorite_genre(self, User):
        g = db.session.query(Genre).get(User.favorite_genre)
        return g.name