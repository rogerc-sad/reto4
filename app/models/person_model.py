from models import db
from sqlalchemy import Integer, String, ForeignKey, Date
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

class AuditMixin(object):
    status = db.Column(db.Integer, nullable=False, default=1)  # 1: activo, 0: inactivo
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    created_by = db.Column(db.Integer, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)


# ------------------------
# PERSONA BASE
# ------------------------
class Persona(db.Model, AuditMixin):
    __tablename__ = 'persona'

    id = db.Column(Integer, primary_key=True)
    primer_nombre = db.Column(String(30), nullable=False)
    segundo_nombre = db.Column(String(30))
    ap_paterno = db.Column(String(30), nullable=False)
    ap_materno = db.Column(String(30))
    ap_casada = db.Column(String(30))
    tipo_documento = db.Column(String(30), nullable=False)
    numero_documento = db.Column(String(20), unique=True, nullable=False)
    genero = db.Column(String(5), nullable=False)
    nacionalidad = db.Column(String(30), nullable=False)
    numero_celular = db.Column(String(20))

    usuario = db.relationship("Usuario", back_populates="persona", uselist=False)

    def serialize(self):
        return {
            'id': self.id,
            'primer_nombre': self.primer_nombre,
            'segundo_nombre': self.segundo_nombre,
            'ap_paterno': self.ap_paterno,
            'ap_materno': self.ap_materno,
            'ap_casada': self.ap_casada,
            'tipo_documento': self.tipo_documento,
            'numero_documento': self.numero_documento,
            'genero': self.genero,
            'nacionalidad': self.nacionalidad,
            'numero_celular': self.numero_celular,
            'status': self.status
        }

    def fullName(self):
        parts = filter(None, [
            self.primer_nombre,
            self.segundo_nombre,
            self.ap_paterno,
            f"DE {self.ap_casada}" if self.ap_casada else None,
            self.ap_materno
        ])
        return " ".join(parts)

# ------------------------
# USUARIOS Y CLIENTES
# ------------------------
class Usuario(db.Model, AuditMixin):
    __tablename__ = 'usuario'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    persona_id = db.Column(Integer, db.ForeignKey('persona.id'), nullable=False)

    username = db.Column(String(30), unique=True, nullable=False)
    password = db.Column(String(255), nullable=False)

    persona = db.relationship("Persona", back_populates="usuario", uselist=False)

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "persona": self.persona.serialize() if self.persona else None,
            "status": self.status
        }


class Producto(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=1)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "status": self.status
        }
