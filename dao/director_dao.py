from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session
        self.v = 4

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_page(self, page):
        pg = self.v * (int(page) - 1)
        return self.session.query(Director).limit(self.v).offset(pg)

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
