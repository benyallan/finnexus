from src.app import create_app
from flask import Flask, jsonify

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
