from flask import Flask

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)

    @app.route('/')
    def home():
        return {"message": "Auth Service Running!"}

    return app
