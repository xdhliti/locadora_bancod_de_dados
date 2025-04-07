from flask import Flask
from config import Config
from extensions import db, migrate
from flask_cors import CORS  # Caso precise de CORS para integração com o frontend

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)  # Ativa CORS, se necessário
    
    # Registra os blueprints
    from routes.cliente_routes import bp as cliente_bp
    app.register_blueprint(cliente_bp, url_prefix='/api/clientes')
    
    from routes.filme_routes import bp as filme_bp
    app.register_blueprint(filme_bp, url_prefix='/api/filmes')
    
    from routes.funcionario_routes import bp as funcionario_bp
    app.register_blueprint(funcionario_bp, url_prefix='/api/funcionarios')
    
    from routes.locacao_routes import bp as locacao_bp
    app.register_blueprint(locacao_bp, url_prefix='/api/locacoes')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
