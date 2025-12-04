# from models.person_model import Persona, Usuario, Rol
# from utils.jwt_util import generate_token, add_token_to_blacklist
# from flask_jwt_extended import create_access_token
# from models import db

# from datetime import date
# from datetime import timedelta
# import bcrypt

# def login_user(username: str, password: str):
#     try:
#         user: Usuario = Usuario.query.filter_by(username=username).first()
#         person: Persona = Persona.query.filter_by(id=user.id_persona).first() if user else None
        
#         if not user:
#             return {'message': 'Usuario no encontrado'}, 404

#         # Validar contraseña con bcrypt
#         if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
#             return {'message': 'Contraseña incorrecta'}, 401
        
#         # Generar token
#         # token = create_access_token(identity=str(user.id_usuario))
#         expires = timedelta(minutes=1440)
#         # expires = timedelta(seconds=18)
#         token = create_access_token(identity=str(user.id_persona), expires_delta=expires)
#         roles = [{'nombre':rol.nombre_rol, "json_data": rol.json_data} for rol in user.rol] if user.rol else []

#         return {
#             'message': 'Login exitoso',
#             'token': token,
#             'user': {
#                 'fullName': f'{person.primer_nombre} {person.ap_paterno}' if person else '',
#                 'id': user.id_persona,
#                 'username': user.username,
#                 'roles': roles
#             }
#         }, 200

#     except Exception as e:
#         return {'message': f'Error al iniciar sesión: {str(e)}'}, 500
    
# @staticmethod
# def logout_user(jti: str):
#     add_token_to_blacklist(jti)
    
    
    
    
from models import Usuario
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from utils.jwt_util import generate_token, add_token_to_blacklist

class AuthService:

    @staticmethod
    def login(username, password):
        user = Usuario.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            return {"message": "Credenciales incorrectas"}, 401

        token = create_access_token(identity=user.id)

        return {
            "access_token": token,
            "usuario_id": user.id
        }, 200

    @staticmethod
    def logout(jti: str):
        add_token_to_blacklist(jti)
        return {"message": "Logout exitoso"}, 200
