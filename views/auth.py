from flask import request, jsonify
from flask_restx import Resource, Namespace

from implemented import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        data = request.json
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")
        favorite_genre = data.get("favorite_genre")

        if None not in [email, password, name, favorite_genre]:
            if user_service.register(email, password, name, favorite_genre):
                return 'пользователь зарегистрирован', 201
        return 'пользователь существует или ввели не верно данные', 400


@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if None is [email, password]:
            return 'не верно', 400

        user = user_service.get_email(email)
        if email == user.email:
            if user_service.compare_passwords(user.password, password):
                tokens = auth_service.generate_tokens(email, password)
                return jsonify(tokens)
        return 'неверный пароль', 400

    @auth_service.auth_check_token
    def put(self):
        data = request.headers["Authorization"]
        new_tokens = auth_service.approve_refresh_token(data)
        return jsonify(new_tokens), 204
