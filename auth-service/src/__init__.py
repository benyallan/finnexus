from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")

    return app
