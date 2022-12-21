from dao.model.movie import Movie
from sqlalchemy import desc


class MovieDAO:
    def __init__(self, session):
        self.session = session
        self.v = 3

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_status(self):
        return self.session.query(Movie).order_by(desc(Movie.year)).all()

    def get_by_satus_page(self, page):
        pg = self.v * (int(page) - 1)
        return self.session.query(Movie).order_by(desc(Movie.year)).limit(self.v).offset(pg)

    def get_by_page(self, page):
        pg = self.v * (int(page) - 1)
        return self.session.query(Movie).limit(self.v).offset(pg)

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
