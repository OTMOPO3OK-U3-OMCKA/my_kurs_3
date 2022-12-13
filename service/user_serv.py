from dao.user_dao import UserDAO
import hashlib
import base64
import hmac
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao
        self.my_email = None

    def get_my_email(self):
        return self.dao.get_email(self.my_email)

    def get_all(self):
        return self.dao.get_all()

    def updater(self, new_user):
        if self.dao.get_email(self.my_email) is None:
            return None
        return self.dao.updater(self.my_email, new_user)

    def get_email(self, email):
        return self.dao.get_email(email)

    def get_genre(self, genre):
        return self.dao.get_genre(genre)

    def update_password(self, my_password):
        password = self.get_hash(my_password)
        return self.dao.update_password(self.my_email, password)

    def register(self, email, password, name, genre):
        if self.get_email(email) is None:
            hash_password = self.get_hash(password)
            favorite_genre = self.get_genre(genre)
            if favorite_genre is None:
                return False
            self.dao.register(email, hash_password, name, favorite_genre)
            return True
        return False

    def get_hash(self, password):
        d = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(d)

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )

    def add_favorite(self, id_movie):
        user = self.get_my_email()
        return self.dao.add_faforite(user.id, id_movie)

    def delete_favorite(self, id_movie):
        user = self.get_my_email()
        return self.dao.delete_favorite(user.id, id_movie)
