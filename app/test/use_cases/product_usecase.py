# use_cases/product_usecase.py
from services.product_service import ProductService

class ProductUseCase:
    def __init__(self):
        self.service = ProductService()

    def list_products(self):
        """Listar todos los productos"""
        products = self.service.get_all()
        return [p.serialize() for p in products]

    def get_product(self, product_id):
        """Obtener producto por ID"""
        product = self.service.get_by_id(product_id)
        return product.serialize() if product else None

    def create_product(self, data):
        """Crear un nuevo producto"""
        product = self.service.create(data)
        return product.serialize()

    def update_product(self, product_id, data):
        """Actualizar producto existente"""
        product = self.service.update(product_id, data)
        return product.serialize() if product else None

    def delete_product(self, product_id):
        """Eliminar producto"""
        return self.service.delete(product_id)
