from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from dao.user_dao import UserDAO
from service.director_serv import DirectorService
from service.genre_serv import GenreService
from service.movie_serv import MovieService
from service.user_serv import UserService
from service.auth_serv import AuthService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
