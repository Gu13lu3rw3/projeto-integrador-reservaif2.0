from flask import Flask
from routes import routes

# aqui eu inicializo o flask
app = Flask(__name__)

# nessa parte eu chamo a função que registra todas as rotas que eu criei
routes.adicionar_rotas(app=app)

# aqui é onde eu rodo o servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
