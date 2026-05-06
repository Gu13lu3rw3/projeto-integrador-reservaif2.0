from flask import render_template
from models.dados import notificacoes

def listar_notificacoes():
    return render_template('notificacoes.html', notificacoes=notificacoes)
