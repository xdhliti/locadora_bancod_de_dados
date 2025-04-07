from extensions import db

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50))
    
    # Relacionamento com locação (um funcionário pode registrar várias locações)
    locacoes = db.relationship('Locacao', backref='funcionario', lazy=True)
