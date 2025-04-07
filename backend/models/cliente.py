from extensions import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    
    # Relacionamento com locação (um cliente pode ter várias locações)
    locacoes = db.relationship('Locacao', backref='cliente', lazy=True)
