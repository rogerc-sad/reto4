# Ejecucion

### Creacion de entorno virtual

Crear carpeta de entorno virtual de python

`python -m venv .venv`

`py -3.9 -m venv .venv`

Por defecto usara la version de python que se tenga instalada, se reconmienda usar las versiones 3.9 a 3.9.12

Para habilitar el entorno

`source .venv/bin/activate`

`source .env`
`source .venv/Scripts/activate`

`python -m pip install --upgrade pip`

Nota: es diferente para windows, se recomienda revisar la documentacion

### Instalar dependencias

`pip install -r requirements.txt`

### Actualizar el archivo de dependencias

`pip freeze > requirements.txt`

### Levantar App

Levantar de forma nativa

`python app/app.py`

Levantar con gunicorn

`pip install gunicorn`
`cd app`
`gunicorn -w 2 --bind 0.0.0.0:5013 --timeout 1200 --access-logfile aplication.log --error-logfile error.log wsgi:app`
