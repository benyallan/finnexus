from flask import jsonify

def init_routes(app):
    # Rota raiz (/)
    @app.route('/', methods=['GET'])
    def root():
        return jsonify({"message": "Bem-vindo à API!"})

    # Rota /hello
    @app.route('/hello', methods=['GET'])
    def hello():
        return jsonify({"message": "Olá, mundo!"})
