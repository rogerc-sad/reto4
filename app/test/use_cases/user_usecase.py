# use_cases/user_usecase.py
from services.user_service import UserService

class UserUseCase:
    def __init__(self):
        self.service = UserService()

    def list_users(self):
        """Listar todos los usuarios"""
        users = self.service.get_all()
        return [u.serialize() for u in users]

    def get_user(self, user_id):
        """Obtener un usuario por ID"""
        user = self.service.get_by_id(user_id)
        return user.serialize() if user else None

    def create_user(self, data):
        """Crear un nuevo usuario"""
        user = self.service.create(data)
        return user.serialize()

    def update_user(self, user_id, data):
        """Actualizar usuario existente"""
        user = self.service.update(user_id, data)
        return user.serialize() if user else None

    def delete_user(self, user_id):
        """Eliminar un usuario"""
        return self.service.delete(user_id)
