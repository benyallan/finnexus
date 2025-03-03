from flask import Flask
from src.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Registrar Blueprint de autenticação
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
