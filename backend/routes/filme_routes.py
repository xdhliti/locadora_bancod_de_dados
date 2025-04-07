from flask import Blueprint, jsonify, request
from extensions import db
from models.filme import Filme

bp = Blueprint('filme_routes', __name__)

# Listar todos os filmes
@bp.route('', methods=['GET'])
def listar_filmes():
    filmes = Filme.query.all()
    resultado = [{
        'id': filme.id,
        'titulo': filme.titulo,
        'genero': filme.genero,
        'ano_lancamento': filme.ano_lancamento,
        'disponibilidade': filme.disponibilidade
    } for filme in filmes]
    return jsonify(resultado), 200

# Criar um novo filme
@bp.route('', methods=['POST'])
def criar_filme():
    data = request.get_json()
    if not data or not data.get('titulo'):
        return jsonify({'error': 'O campo "titulo" é obrigatório.'}), 400

    filme = Filme(
        titulo=data.get('titulo'),
        genero=data.get('genero'),
        ano_lancamento=data.get('ano_lancamento'),
        disponibilidade=data.get('disponibilidade')
    )
    db.session.add(filme)
    db.session.commit()
    return jsonify({
        'id': filme.id,
        'titulo': filme.titulo,
        'genero': filme.genero,
        'ano_lancamento': filme.ano_lancamento,
        'disponibilidade': filme.disponibilidade
    }), 201
