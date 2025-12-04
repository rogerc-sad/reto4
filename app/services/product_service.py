from models.person_model import Producto
from models import db

class ProductService:

    @staticmethod
    def get_all_products():
        products = Producto.query.all()
        return [p.serialize() for p in products]

    @staticmethod
    def get_product(product_id):
        product = Producto.query.get(product_id)
        if not product:
            return None
        return product.serialize()

    @staticmethod
    def create_product(data):
        product = Producto(
            nombre=data['nombre'],
            descripcion=data.get('descripcion'),
            precio=data['precio'],
            stock=data.get('stock', 0)
        )
        db.session.add(product)
        db.session.commit()
        return {"message": "Producto creado correctamente", "id": product.id}, 201

    @staticmethod
    def update_product(product_id, data):
        product = Producto.query.get(product_id)
        if not product:
            return {"message": "Producto no encontrado"}, 404

        product.nombre = data.get("nombre", product.nombre)
        product.descripcion = data.get("descripcion", product.descripcion)
        product.precio = data.get("precio", product.precio)
        product.stock = data.get("stock", product.stock)

        db.session.commit()
        return {"message": "Producto actualizado correctamente"}, 200

    @staticmethod
    def delete_product(product_id):
        product = Producto.query.get(product_id)
        if not product:
            return {"message": "Producto no encontrado"}, 404
        db.session.delete(product)
        db.session.commit()
        return {"message": "Producto eliminado correctamente"}, 200
