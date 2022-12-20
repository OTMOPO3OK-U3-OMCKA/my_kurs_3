import pytest
from unittest.mock import MagicMock
from dao.model.user import User
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.user_dao import UserDAO
from service.user_serv import UserService
from unittest.mock import MagicMock
from views.user import request
import responses

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
    u = User(id=4, name="Rater", email="kot@mail.com", password="1234", favorite_genre="Комедия")
    serv.my_email = MagicMock(return_value="kot@mail.com")
    serv.get_my_email = MagicMock(return_value=u)
    return serv


dd = [({"status": "new", "page": "1"}, 3),
      ({"status": "new"}, 4),
      ({"page": "3"}, 3),
      ({"status": 2, "page": 1}, 3),
      (None, 3)]

class TestApi:
    @pytest.fixture(autouse=True)
    def est_a(self, serv):
        self.serv = serv

    @pytest.mark.skip()
    def test_api(self, est_a):
        app2 = app
        app2
        self.serv.my_email = "kot@mail.com"
        response = app2.test_client().get('/user/')
        assert response.status_code == 200

    def test_tt(self):
        w = self.serv.get_my_email()
        assert w.id == 4

    def test_views_users(self):
        re = app.test_client().get('/users/')
        assert re.status_code == 200
        assert re.json != 0

    @pytest.mark.parametrize('par, len_json', dd)
    def test_views_get_movies(self, par, len_json):
        re = app.test_client().get('/movies/', query_string=par)
        assert re.status_code == 200
        if par is not None:
            assert len(re.json) == len_json
        else:
            assert len(re.json) != len_json

    @pytest.mark.skip()
    def test_views_post_movies(self):
        data = {"title": "oo"}
        re = app.test_client().post('/movies/', json=data, follow_redirects=True)
        assert re.json == ""
        assert re.status_code == 201


    def test_views_put_movies_id(self):
        data = {"id": 22, "title": "rrr"}
        re = app.test_client().put('/movies/', json=data, follow_redirects=True)
        assert re.status_code == 200

    def test_views_delete_movies_id(self):
        re = app.test_client().delete('/movies/22/', query_string="22")
        assert re.status_code == 204
