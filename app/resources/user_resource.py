from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from services.user_service import UserService


create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('primer_nombre', type=str, required=True)
create_user_parser.add_argument('segundo_nombre', type=str)
create_user_parser.add_argument('ap_paterno', type=str, required=True)
create_user_parser.add_argument('ap_materno', type=str)
create_user_parser.add_argument('ap_casada', type=str)
create_user_parser.add_argument('tipo_documento', type=str, required=True)
create_user_parser.add_argument('numero_documento', type=str, required=True)
create_user_parser.add_argument('genero', type=str, required=True, choices=['M', 'F', 'O', 'N/A'], default='N/A')
create_user_parser.add_argument('nacionalidad', type=str, required=True)
create_user_parser.add_argument('numero_celular', type=str)
create_user_parser.add_argument('username', type=str)
create_user_parser.add_argument('password', type=str)

update_user_parser = create_user_parser.copy()


class Users(Resource):

    @jwt_required()
    def get(self):
        return UserService.get_all_users(), 200

    @jwt_required()
    def post(self):
        data = create_user_parser.parse_args()
        return UserService.create_user(data)


class User(Resource):

    @jwt_required()
    def get(self, user_id):
        user = UserService.get_user(user_id)
        if not user:
            return {"message": "Usuario no encontrado"}, 404
        return user, 200

    @jwt_required()
    def put(self, user_id):
        data = update_user_parser.parse_args()
        return UserService.update_user(user_id, data)

    @jwt_required()
    def delete(self, user_id):
        return UserService.delete_user(user_id)
