import os
from flask import Flask
from routes.routes import adicionar_rotas

# Configuração simples de templates
template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Chamada da função de rotas conforme solicitado
adicionar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
