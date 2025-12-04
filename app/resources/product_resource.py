from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from services.product_service import ProductService

parser = reqparse.RequestParser()
parser.add_argument("nombre", type=str, required=True)
parser.add_argument("descripcion", type=str)
parser.add_argument("precio", type=float, required=True)
parser.add_argument("stock", type=int)

class Products(Resource):
    @jwt_required()
    def get(self):
        return ProductService.get_all_products()

    @jwt_required()
    def post(self):
        data = parser.parse_args()
        return ProductService.create_product(data)

class Product(Resource):
    @jwt_required()
    def get(self, product_id):
        product = ProductService.get_product(product_id)
        if not product:
            return {"message": "Producto no encontrado"}, 404
        return product

    @jwt_required()
    def put(self, product_id):
        data = parser.parse_args()
        return ProductService.update_product(product_id, data)

    @jwt_required()
    def delete(self, product_id):
        return ProductService.delete_product(product_id)
