from flask import Blueprint, jsonify, request
from extensions import db
from models.cliente import Cliente

bp = Blueprint('cliente_routes', __name__)

# Listar todos os clientes
@bp.route('', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    resultado = [{
        'id': cliente.id,
        'nome': cliente.nome,
        'endereco': cliente.endereco,
        'telefone': cliente.telefone,
        'email': cliente.email
    } for cliente in clientes]
    return jsonify(resultado), 200

# Criar um novo cliente
@bp.route('', methods=['POST'])
def criar_cliente():
    data = request.get_json()
    if not data or not data.get('nome'):
        return jsonify({'error': 'O campo "nome" é obrigatório.'}), 400

    cliente = Cliente(
        nome = data.get('nome'),
        endereco = data.get('endereco'),
        telefone = data.get('telefone'),
        email = data.get('email')
    )
    db.session.add(cliente)
    db.session.commit()
    return jsonify({
        'id': cliente.id,
        'nome': cliente.nome,
        'endereco': cliente.endereco,
        'telefone': cliente.telefone,
        'email': cliente.email
    }), 201
