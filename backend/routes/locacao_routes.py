from flask import Blueprint, jsonify, request
from datetime import datetime
from extensions import db
from models.locacao import Locacao
from models.cliente import Cliente
from models.filme import Filme
from models.funcionario import Funcionario

bp = Blueprint('locacao_routes', __name__)

# Listar todas as locações
@bp.route('', methods=['GET'])
def listar_locacoes():
    locacoes = Locacao.query.all()
    resultado = []
    for l in locacoes:
        resultado.append({
            'id': l.id,
            'cliente': l.cliente.nome if l.cliente else None,
            'filme': l.filme.titulo if l.filme else None,
            'funcionario': l.funcionario.nome if l.funcionario else None,
            'data_locacao': l.data_locacao.isoformat() if l.data_locacao else None,
            'data_devolucao_prevista': l.data_devolucao_prevista.isoformat() if l.data_devolucao_prevista else None,
            'data_devolucao_real': l.data_devolucao_real.isoformat() if l.data_devolucao_real else None,
            'valor_aluguel': str(l.valor_aluguel) if l.valor_aluguel is not None else None,
            'multa': str(l.multa) if l.multa is not None else None
        })
    return jsonify(resultado), 200

# Criar uma nova locação
@bp.route('', methods=['POST'])
def criar_locacao():
    data = request.get_json()
    
    # Verifica se os dados essenciais estão presentes
    if not data or not data.get('id_cliente') or not data.get('id_filme') or not data.get('id_funcionario'):
        return jsonify({'error': 'Campos id_cliente, id_filme e id_funcionario são obrigatórios.'}), 400

    cliente = Cliente.query.get(data.get('id_cliente'))
    filme = Filme.query.get(data.get('id_filme'))
    funcionario = Funcionario.query.get(data.get('id_funcionario'))
    
    if not cliente or not filme or not funcionario:
        return jsonify({'error': 'Cliente, Filme ou Funcionário não encontrado.'}), 404
    
    # Trata as datas
    def parse_date(field):
        date_str = data.get(field)
        if date_str:
            try:
                return datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                return None
        return None

    data_locacao = parse_date('data_locacao') or datetime.today().date()
    data_devolucao_prevista = parse_date('data_devolucao_prevista')
    data_devolucao_real = parse_date('data_devolucao_real')
    
    locacao = Locacao(
        id_cliente = cliente.id,
        id_filme = filme.id,
        id_funcionario = funcionario.id,
        data_locacao = data_locacao,
        data_devolucao_prevista = data_devolucao_prevista,
        data_devolucao_real = data_devolucao_real,
        valor_aluguel = data.get('valor_aluguel'),
        multa = data.get('multa')
    )
    db.session.add(locacao)
    db.session.commit()
    
    return jsonify({
        'id': locacao.id,
        'cliente': cliente.nome,
        'filme': filme.titulo,
        'funcionario': funcionario.nome,
        'data_locacao': locacao.data_locacao.isoformat(),
        'data_devolucao_prevista': locacao.data_devolucao_prevista.isoformat() if locacao.data_devolucao_prevista else None,
        'data_devolucao_real': locacao.data_devolucao_real.isoformat() if locacao.data_devolucao_real else None,
        'valor_aluguel': str(locacao.valor_aluguel),
        'multa': str(locacao.multa)
    }), 201
