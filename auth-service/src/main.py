from __init__ import create_app
from flask import jsonify

app = create_app()

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, mundo!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)