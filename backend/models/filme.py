from extensions import db

class Filme(db.Model):
    __tablename__ = 'filme'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.String(50))
    ano_lancamento = db.Column(db.Integer)
    disponibilidade = db.Column(db.Integer)  # Quantidade de cópias disponíveis
    
    # Relacionamento com locação (um filme pode ter várias locações)
    locacoes = db.relationship('Locacao', backref='filme', lazy=True)
