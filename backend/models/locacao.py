from datetime import date
from extensions import db

class Locacao(db.Model):
    __tablename__ = 'locacao'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Chaves estrangeiras para as entidades envolvidas
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    id_filme = db.Column(db.Integer, db.ForeignKey('filme.id'), nullable=False)
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    
    data_locacao = db.Column(db.Date, nullable=False, default=date.today)
    data_devolucao_prevista = db.Column(db.Date)
    data_devolucao_real = db.Column(db.Date, nullable=True)
    
    valor_aluguel = db.Column(db.Numeric(10,2))
    multa = db.Column(db.Numeric(10,2))
