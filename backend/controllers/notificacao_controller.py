from flask import render_template, request, redirect, url_for, session
from models import dados


def listar_notificacoes():
    perfil = session['usuario']['perfil']
    if perfil == 'Coordenador' or perfil == 'Administrador' or perfil == 'Admin':
        notificacoes = dados.listar_todas_notificacoes()
    else:
        notificacoes = dados.listar_notificacoes_do_usuario(session['usuario']['id'])
    return render_template('notificacoes.html', notificacoes=notificacoes)


def marcar_como_lida():
    id_notificacao = int(request.args.get('id'))
    dados.marcar_notificacao_como_lida(id_notificacao)
    return redirect(url_for('listar_notificacoes'))


def deletar_notificacao():
    id_notificacao = int(request.args.get('id'))
    dados.deletar_notificacao_do_banco(id_notificacao)
    return redirect(url_for('listar_notificacoes'))
