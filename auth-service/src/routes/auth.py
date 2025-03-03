from flask import Blueprint, request, jsonify
import ulid
from src.models.user import User
from src.database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Verificar se os campos obrigatórios estão presentes
    required_fields = ['name', 'email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Criar ID ULID para o usuário
    user_id = str(ulid.new())

    # Criar usuário
    user = User(
        id=user_id,
        name=data['name'],
        email=data['email'],
        password=data['password']  # Hash da senha será tratado depois
    )

    # Salvar no banco
    db.users.insert_one(user.to_dict())

    return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
