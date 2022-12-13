from flask_restx import Resource, Namespace

from implemented import user_service, auth_service

favorite_ns = Namespace('favorites/movies')


@favorite_ns.route('/<m_id>')
class FavoriteView(Resource):
    @auth_service.auth_check_token
    def post(self, m_id):
        return user_service.add_favorite(m_id), 201

    @auth_service.auth_check_token
    def delete(self, m_id):
        return user_service.delete_favorite(m_id), 204
