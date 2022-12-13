from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        page = request.args.get("page")
        rs = director_service.get_all(page)
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = director_service.get_my_email()
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
