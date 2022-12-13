from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("status") == "new":
            if str(filters.get("page")).isdigit():
                movies = self.dao.get_by_satus_page(filters.get("page"))
            else:
                movies = self.dao.get_by_status()
        elif str(filters.get("page")).isdigit():
            movies = self.dao.get_by_page(filters.get("page"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
