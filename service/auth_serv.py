from implemented import UserService
from flask import abort, request
import datetime
import calendar
import jwt
from config import Config
c = Config()
ALGORITHM = c.ALGORITHM
SECRET_HERE = c.SECRET_HERE


class AuthService:
    def __init__(self, serv: UserService):
        self.serv = serv

    def get_email(self, email):
        return self.serv.get_email(email)

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.serv.get_email(email)

        if user is None:
            raise abort(401)

        if not is_refresh:
            if not self.serv.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email
        }
        mins30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(mins30.timetuple())
        access_token = jwt.encode(data, key=SECRET_HERE, algorithm=ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=SECRET_HERE, algorithm=ALGORITHM)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return tokens

    def approve_refresh_token(self, d):
        try:
            refresh_token = d.split('Bearer ')[-1]
            data = jwt.decode(jwt=refresh_token, key=SECRET_HERE, algorithms=[ALGORITHM])
            email = data.get("email")

            return self.generate_tokens(email, None, is_refresh=True)
        except Exception as e:
            print(e)
            abort(403)

    def auth_required(self, func):
        def wrapper(*args, **kwargs):
            if "Authorization" not in request.headers:
                abort(401)

            return func(*args, **kwargs)
        return wrapper

    def auth_check_token(self, func):
        def wrapper(*args, **kwargs):
            if "Authorization" not in request.headers:
                abort(401)

            try:
                full_token = request.headers.get("Authorization")
                token = full_token.split("Bearer ")[-1]
                data = jwt.decode(token, key=SECRET_HERE, algorithms=ALGORITHM)
                self.serv.my_email = data.get("email")

            except Exception as e:
                print(e)
                abort(403)
            return func(*args, **kwargs)
        return wrapper

    def add_favorite(self, m_id):
        return self.serv.add_favorite(m_id)

    def delete_favorite(self, m_id):
        return self.serv.delete_favorite(m_id)

