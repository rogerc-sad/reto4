# from werkzeug.security import generate_password_hash
# from flask_restful import Resource, reqparse
# from flask import jsonify
# from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity

# import services.auth_services as AuthService
# from models.person_model import Persona, Usuario

# parseUserLogin = reqparse.RequestParser()
# parseUserLogin.add_argument('username', type=str, required=True, help='Debe ingresar el nombre de usuario')
# parseUserLogin.add_argument('password', type=str, required=True, help='Debe ingresar una contraseña')
# class Login(Resource):
#     def post(self):
#         data = parseUserLogin.parse_args()
#         response, status = AuthService.login_user(data['username'], data['password'])
#         return response, status

# class Logout(Resource):
#     @jwt_required()
#     def post(self):
#         jti = get_jwt()["jti"] 
#         AuthService.logout_user(jti) 
#         return {"message": "Sesión cerrada exitosamente"}, 200
    
# class CurrentUser(Resource):
#     @jwt_required()
#     def post(self):
#         user_id = get_jwt_identity()
#         persona = Persona.query.get(user_id)
#         usuario = Usuario.query.get(user_id)
#         if not persona or not usuario:
#             return {"message": "Usuario no encontrado"}, 404

#         return {
#             "id": user_id,
#             "username": usuario.username,
#             "cargo": usuario.cargo,
#             "persona": {
#                 "primer_nombre": persona.primer_nombre,
#                 "ap_paterno": persona.ap_paterno,
#                 "ap_materno": persona.ap_materno,
#                 "numero_documento": persona.numero_documento
#             }
#         }, 200

from flask_restful import Resource, reqparse
from services.auth_services import AuthService
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity


login_parser = reqparse.RequestParser()
login_parser.add_argument("username", type=str, required=True)
login_parser.add_argument("password", type=str, required=True)

class Login(Resource):

    def post(self):
        data = login_parser.parse_args()
        return AuthService.login(data["username"], data["password"])

class Logout(Resource):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"] 
        return AuthService.logout(jti)
