from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db
from core import configuration
from datetime import timedelta
from resources.user_resource import Users, User
from resources.product_resource import Products, Product
from datetime import timedelta

import resources.auth_resource as Auth


def create_app():
    app = Flask(__name__, static_folder=None)

    # CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Configuración Flask
    app.config['SQLALCHEMY_DATABASE_URI'] = configuration.SQLALCHEMY_DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = configuration.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=120)
    app.secret_key = configuration.APP_SECRET_KEY

    # Inicializar extensiones
    db.init_app(app)
    jwt = JWTManager(app)
    api = Api(app)

    # RUTAS
    
    # Gestión de usuarios
    api.add_resource(User, '/users')                # GET, POST
    api.add_resource(Users, '/users/<int:user_id>')   # GET, PUT, DELETE

    # Autenticación
    api.add_resource(Auth.Login, '/auth/login')           # POST
    api.add_resource(Auth.Logout, '/auth/logout')         # POST
    
    # Products
    api.add_resource(Products, '/products')
    api.add_resource(Product, '/products/<int:product_id>')
   
    return app
