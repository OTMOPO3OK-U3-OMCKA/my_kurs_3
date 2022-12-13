from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

users_ns = Namespace('users')

@users_ns.route("/")
class UserView(Resource):
    def get(self):
        sss = user_service.get_all()
        return UserSchema(many=True).dump(sss), 200