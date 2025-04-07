from flask import Blueprint, jsonify, request
from extensions import db
from models.funcionario import Funcionario

bp = Blueprint('funcionario_routes', __name__)

# Listar todos os funcionários
@bp.route('', methods=['GET'])
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    resultado = [{
        'id': funcionario.id,
        'nome': funcionario.nome,
        'cargo': funcionario.cargo
    } for funcionario in funcionarios]
    return jsonify(resultado), 200

# Criar um novo funcionário
@bp.route('', methods=['POST'])
def criar_funcionario():
    data = request.get_json()
    if not data or not data.get('nome'):
        return jsonify({'error': 'O campo "nome" é obrigatório.'}), 400

    funcionario = Funcionario(
        nome = data.get('nome'),
        cargo = data.get('cargo')
    )
    db.session.add(funcionario)
    db.session.commit()
    return jsonify({
        'id': funcionario.id,
        'nome': funcionario.nome,
        'cargo': funcionario.cargo
    }), 201
