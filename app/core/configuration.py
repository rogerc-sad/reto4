import os

APP_VERSION = os.getenv("APP_VERSION", "0.0.1")

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL','postgresql://postgres:postgres@localhost:5432/marketplace')
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "secret")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "confidential")
TOKEN_MINUTES_LIFE_ADMIN=os.getenv("DBUSER", 60)

API_SECRET_KEY = os.getenv("API_SECRET_KEY", "f")
API_URL = os.getenv("API_URL", "f")

SERVER_HOST = os.environ.get("SERVER_HOST", '0.0.0.0') 
SERVER_PORT = int(os.environ.get("SERVER_PORT", "5000"))
DEBUG = os.environ.get("DEBUG", "true") == "true"

WS_API_SECRET_KEY = os.getenv("API_SECRET_KEY", "")

class Config:
    APP_SECRET_KEY = os.getenv('APP_SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/marketplace')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 5000
    DEBUG = True
