import pytest
from unittest.mock import MagicMock
from dao.model.user import User
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.user_dao import UserDAO
from service.user_serv import UserService


@pytest.fixture()
def dao_user():
    dao_user = UserDAO(None)

    u1 = User(id=4, name="Rater", email="rater@gmail.com", password="1234", favorite_genre="Комедия")
    u2 = User(id=7, name="Igor", email="igor@gmail.com", password="3456", favorite_genre="Боевик")
    u3 = User(id=9, name="Tor", email="tor@gmail.com", password="6789", favorite_genre="Комедия")

    g1 = Genre(id=1, name="Комедия")

    dao_user.get_all = MagicMock(return_value=[u1, u2, u3])
    dao_user.get_email = MagicMock(return_value=u3)
    dao_user.get_genre = MagicMock(return_value=g1.id)
    dao_user.updater_u = MagicMock(return_value=u1)
    dao_user.updater = MagicMock(return_value=u3)
    dao_user.get_hash = MagicMock(return_value="hash")

    return dao_user


@pytest.fixture()
def dao_user_if_get_email_return_none():
    dao_user = UserDAO(None)
    dao_user.get_email = MagicMock(return_value=None)
    dao_user.get_genre = MagicMock(return_value=None)
    dao_user.register = MagicMock(return_value="000")

    return dao_user

@pytest.fixture()
def dao_user_if_get_hash():
    dao_user = UserDAO(None)
    dao_user.get_email = MagicMock(return_value=None)
    dao_user.get_genre = MagicMock(return_value="999")
    dao_user.register = MagicMock(return_value="000")

    return dao_user


class TestUserDao:
    @pytest.fixture(autouse=True)
    def user_service(self, dao_user, dao_user_if_get_email_return_none, dao_user_if_get_hash):
        self.user_service = UserService(dao_user)
        self.dao_user_if_get_email_return_none = UserService(dao_user_if_get_email_return_none)
        self.register = UserService(dao_user_if_get_hash)
        self.register.get_hash = MagicMock(return_value="000")

    def test_user_get_my_email(self):
        u = self.user_service.get_my_email()
        assert u.id == 9
        assert self.dao_user_if_get_email_return_none.get_my_email() is None

    def test_user_get_all(self):
        u = self.user_service.get_all()
        assert type(u) is list

    def test_user_get_email(self):
        u = self.user_service.get_email(1)
        assert type(u.email) is str
        assert self.dao_user_if_get_email_return_none.get_my_email() is None

    def test_user_get_genre(self):
        u = self.user_service.get_genre(1)
        assert u == 1
        assert self.dao_user_if_get_email_return_none.get_genre(1) is None

    def test_user_updater(self):
        us = self.user_service.get_email(1)
        assert self.user_service.updater(1) == us
        assert self.dao_user_if_get_email_return_none.updater(1) is None

    def test_user_get_hash(self):
        test_hash = self.user_service.get_hash("4stuth5779")
        assert type(test_hash) == bytes

    def test_user_register(self):
        assert self.dao_user_if_get_email_return_none.register(1, "2", 3, 4) is True
        assert self.user_service.register(1, "2", 3, 4) is False
        assert self.register.register(1, "rt356", "3", 4) is True

    def test_user_compare_password(self):
        g = "777"
        g1 = self.dao_user_if_get_email_return_none.get_hash(g)
        assert self.user_service.compare_passwords(g1, g) is True
        assert self.user_service.compare_passwords(g1, "t" + g) is False
