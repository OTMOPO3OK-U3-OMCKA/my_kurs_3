from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        page = request.args.get("page")
        rs = genre_service.get_all(page)
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_service.get_my_email()
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
