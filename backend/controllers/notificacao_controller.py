from flask import render_template, request, redirect, session
from models.dados import notificacoes, usuarios, reservas
from datetime import datetime
from controllers.auth_controller import login_required
@login_required
def listar_notificacoes():
    usuario_id = session.get('usuario_id')
    perfil = session.get('usuario_perfil')
    if perfil == 'Coordenador' or perfil == 'Administrador':
        notifs = notificacoes
    else:
        notifs = [n for n in notificacoes if n.get('id_usuario') == usuario_id]
    return render_template('notificacoes.html', notificacoes=notifs)
def criar_notificacao_pedido(id_reserva, id_professor, id_sala, motivo):
    coordenadores = [u for u in usuarios if u['perfil'] == 'Coordenador']
    for coord in coordenadores:
        notificacao = {
            "id": len(notificacoes) + 1,
            "id_usuario": coord['id'],
            "id_reserva": id_reserva,
            "id_professor": id_professor,
            "tipo": "Novo Pedido de Reserva",
            "mensagem": f"Novo pedido de reserva #{id_reserva} recebido. Professor ID: {id_professor}, Sala: {id_sala}, Motivo: {motivo}",
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "lida": False,
            "meio_envio": "in-app"
        }
        notificacoes.append(notificacao)
def criar_notificacao_status(id_professor, mensagem):
    notificacao = {
        "id": len(notificacoes) + 1,
        "id_usuario": id_professor,
        "tipo": "Mudança de Status",
        "mensagem": mensagem,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "lida": False,
        "meio_envio": "in-app"
    }
    notificacoes.append(notificacao)
@login_required
def marcar_como_lida():
    id_notificacao = int(request.args.get('id'))
    for notif in notificacoes:
        if notif.get('id') == id_notificacao:
            notif['lida'] = True
    return redirect('/notificacoes')
@login_required
def deletar_notificacao():
    id_notificacao = int(request.args.get('id'))
    global notificacoes
    notificacoes[:] = [n for n in notificacoes if n.get('id') != id_notificacao]
    return redirect('/notificacoes')
