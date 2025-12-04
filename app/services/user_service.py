from werkzeug.security import generate_password_hash
from models import db, Usuario, Persona
from sqlalchemy.exc import SQLAlchemyError


class UserService:

    @staticmethod
    def create_user(data):
        try:
            persona = Persona(
                primer_nombre=data.get("primer_nombre"),
                segundo_nombre=data.get("segundo_nombre"),
                ap_paterno=data.get("ap_paterno"),
                ap_materno=data.get("ap_materno"),
                ap_casada=data.get("ap_casada"),
                tipo_documento=data.get("tipo_documento"),
                numero_documento=data.get("numero_documento"),
                genero=data.get("genero"),
                nacionalidad=data.get("nacionalidad"),
                numero_celular=data.get("numero_celular")
            )
            db.session.add(persona)
            db.session.flush()

            usuario = Usuario(
                username=data.get("username"),
                password=generate_password_hash(data.get("password")),
                persona_id=persona.id
            )
            db.session.add(usuario)
            db.session.commit()

            return {"message": "Usuario creado correctamente", "id": usuario.id}, 201

        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": f"Error al crear usuario: {str(e)}"}, 500


    @staticmethod
    def get_all_users():
        users = Usuario.query.all()
        return [u.as_dict() for u in users]


    @staticmethod
    def get_user(user_id):
        user = Usuario.query.get(user_id)
        if not user:
            return None
        return user.as_dict()


    @staticmethod
    def update_user(user_id, data):
        try:
            user = Usuario.query.get(user_id)
            if not user:
                return {"message": "Usuario no encontrado"}, 404

            persona = user.persona

            persona.primer_nombre = data.get("primer_nombre", persona.primer_nombre)
            persona.segundo_nombre = data.get("segundo_nombre", persona.segundo_nombre)
            persona.ap_paterno = data.get("ap_paterno", persona.ap_paterno)
            persona.ap_materno = data.get("ap_materno", persona.ap_materno)
            persona.ap_casada = data.get("ap_casada", persona.ap_casada)
            persona.tipo_documento = data.get("tipo_documento", persona.tipo_documento)
            persona.numero_documento = data.get("numero_documento", persona.numero_documento)
            persona.genero = data.get("genero", persona.genero)
            persona.nacionalidad = data.get("nacionalidad", persona.nacionalidad)
            persona.numero_celular = data.get("numero_celular", persona.numero_celular)

            if data.get("username"):
                user.username = data.get("username")

            if data.get("password"):
                user.password = generate_password_hash(data.get("password"))

            db.session.commit()
            return {"message": "Usuario actualizado correctamente"}, 200

        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": f"Error al actualizar usuario: {str(e)}"}, 500


    @staticmethod
    def delete_user(user_id):
        try:
            user = Usuario.query.get(user_id)
            if not user:
                return {"message": "Usuario no encontrado"}, 404

            db.session.delete(user)
            db.session.commit()
            return {"message": "Usuario eliminado correctamente"}, 200

        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": f"Error al eliminar usuario: {str(e)}"}, 500
