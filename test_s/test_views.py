import pytest
from unittest.mock import MagicMock
from dao.model.user import User
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.user_dao import UserDAO
from service.user_serv import UserService
from unittest.mock import MagicMock

from app import app

"""@pytest.fixture()
def serv_user():
    serv_user = UserService(None)

    u1 = User(id=4, name="Rater", email="rater@gmail.com", password="1234", favorite_genre="Комедия")
    u2 = User(id=7, name="Igor", email="igor@gmail.com", password="3456", favorite_genre="Боевик")
    u3 = User(id=9, name="Tor", email="tor@gmail.com", password="6789", favorite_genre="Комедия")

    g1 = Genre(id=1, name="Комедия")

    serv_user.get_my_email = MagicMock(return_value=[u1, u2, u3])
    serv_user.updater = MagicMock(return_value=g1.id)
    serv_user.update_password = MagicMock(return_value="hash")

    return serv_user
"""
@pytest.fixture
def serv():
    serv = UserService(None)
    u1 = User(id=4, name="Rater", email="rater@gmail.com", password="1234", favorite_genre="Комедия")
    serv.get_my_email = MagicMock(return_value=u1)
    return serv


class TestApi:# не могу этот тест сделать декоратор удалял но все равно не работает
    @pytest.fixture(autouse=True)
    def test_a(self, serv):
        self.serv = serv
        self.u1 = User(id=4, name="Rater", email="rater@gmail.com", password="1234", favorite_genre="Комедия")
        self.serv.get_my_email = self.u1

    def test_api(self):
        response = app.test_client().get('/user/')
        s = self.serv.get_my_email
        assert response.status_code == 200
