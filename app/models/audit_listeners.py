from sqlalchemy import event
from datetime import date
from flask_jwt_extended import get_jwt_identity
from models import db

def get_current_user():
    try:
        return get_jwt_identity()  # usuario autenticado (si hay JWT)
    except:
        return "system"  # fallback si no hay usuario

@event.listens_for(db.session, "before_flush")
def set_audit_fields(session, flush_context, instances):
    for obj in session.new:  # registros nuevos
        if hasattr(obj, "fecha_creacion") and not obj.fecha_creacion:
            obj.fecha_creacion = date.today()
        if hasattr(obj, "usuario_creacion") and not obj.usuario_creacion:
            obj.usuario_creacion = get_current_user()

    for obj in session.dirty:  # registros modificados
        if hasattr(obj, "fecha_modificacion"):
            obj.fecha_modificacion = date.today()
        if hasattr(obj, "usuario_modificacion"):
            obj.usuario_modificacion = get_current_user()
