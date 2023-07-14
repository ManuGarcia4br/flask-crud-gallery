import os
SECRET_KEY = 'bilu'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '1234',
        servidor = 'localhost',
        database = 'jogoteca'
        
    )
    
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'