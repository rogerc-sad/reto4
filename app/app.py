import socket

from core.factory import create_app
from models import db
from core import configuration
from logging.handlers import RotatingFileHandler

# Configuración del logger
import logging
from logging.handlers import RotatingFileHandler
import os
import sys

# Configuración del logger
LOG_FILENAME = './aplication.log'

# Asegurarse de que la carpeta exista
os.makedirs(os.path.dirname(LOG_FILENAME), exist_ok=True)

# Crear logger principal
logger = logging.getLogger("MARKETPLACE_APP")
logger.setLevel(logging.DEBUG)  # Captura todo: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Formato para los logs
formatter = logging.Formatter( '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )

# Handler: archivo con rotación
file_handler = RotatingFileHandler( LOG_FILENAME, maxBytes=40_000_000, backupCount=40, encoding='utf-8' )
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Handler: consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)  # todo lo que sea DEBUG o superior se muestra
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Redirigir logs de Flask y otras librerías a este logger
logging.getLogger("werkzeug").handlers = logger.handlers
logging.getLogger("werkzeug").setLevel(logging.DEBUG)

# Ejemplo: ahora todo lo que se haga con logging se verá en consola y se guardará
logger.info("Sistema iniciado correctamente")

app = create_app()

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Esto crea las tablas
    print("Aplicacion iniciada en: http://{}:{}".format(local_ip, configuration.SERVER_PORT))
    app.run(host=configuration.SERVER_HOST,
            port=configuration.SERVER_PORT,
            debug=configuration.DEBUG)

