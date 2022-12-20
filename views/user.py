from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema, UserFullSchema
from implemented import user_service, auth_service

user_ns = Namespace('user')
user_schema = UserSchema()


@user_ns.route("/")
class UserView(Resource):
    def get(self):
        data = user_service.get_my_email()
        if data is None:
            return "", 401
        return UserFullSchema().dump(data), 200

    @auth_service.auth_check_token
    def patch(self):
        user = request.json
        s = user_service.updater(user)
        return user_schema.dump(s), 204


@user_ns.route("/password/")
class UserPasswordView(Resource):
    @auth_service.auth_check_token
    def put(self):
        user = request.json
        user_service.update_password(user.get("password"))
        return "пароль изменен", 204
