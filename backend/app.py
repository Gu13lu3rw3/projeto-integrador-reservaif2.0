import os
from flask import Flask
from routes.routes import adicionar_rotas

template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.secret_key = 'sua_chave_secreta_aqui_mude_em_producao'

adicionar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
