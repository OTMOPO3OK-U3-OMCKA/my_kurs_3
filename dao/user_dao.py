from dao.model.user import User
from dao.model.genre import Genre
from dao.model.favourites import Favourites

class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def register(self, email, password, name, favorite_genre):
        user = User(email=email, password=password, name=name, favorite_genre=favorite_genre)
        self.session.add(user)
        self.session.commit()

    def get_genre(self, genre):
        data = self.session.query(Genre).filter(Genre.name == genre).first()
        return data.id

    def updater(self, email, data):
        user = self.get_email(email)
        if "name" in data:
            user.name = data["name"]
        if "email" in data:
            user.email = data["email"]
        if "favorite_genre" in data:
            user.favorite_genre = self.get_genre(data["favorite_genre"])
        self.session.add(user)
        self.session.commit()
        return user

    def update_password(self, my_email, password):
        user = self.get_email(my_email)
        user.password = password
        self.session.add(user)
        self.session.commit()

    def add_faforite(self, id_user, id_movie):
        f = self.session.query(Favourites).filter(Favourites.user_id == id_user, Favourites.movie_id == id_movie).first()
        if f is None:
            ff = Favourites(user_id=id_user, movie_id=id_movie)
            self.session.add(ff)
            self.session.commit()
            return "добавлен"
        return "уже есть"

    def delete_favorite(self, id_user, id_movie):
        f = self.session.query(Favourites).filter(Favourites.user_id == id_user, Favourites.movie_id == id_movie).first()
        if f is not None:
            self.session.delete(f)
            self.session.commit()

