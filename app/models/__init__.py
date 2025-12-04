from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from models.person_model import Persona, Usuario, Producto
from .audit_listeners import *  # importa para registrar eventos
