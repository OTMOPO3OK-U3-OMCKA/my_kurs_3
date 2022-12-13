from setup_db import db

class Favourites(db.Model):
    __tablename__ = "favourites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    movie = db.relationship("Movie")
