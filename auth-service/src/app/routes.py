from flask import jsonify

def init_routes(app):
    @app.route('/hello', methods=['GET'])
    def hello():
        return jsonify({"message": "Olá, mundo!"})
