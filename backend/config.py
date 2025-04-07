import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Aqui usamos SQLite como exemplo; para outro BD, basta alterar a URI.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
