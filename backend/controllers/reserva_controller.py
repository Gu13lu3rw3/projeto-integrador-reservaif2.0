from flask import render_template, request, redirect, url_for, session
from models import dados
from datetime import datetime, timedelta


def listar_reservas():
    reservas = dados.listar_todas_reservas()
    salas = dados.listar_todas_salas()
    salas_dict = {s.id: s.nome for s in salas}
    for r in reservas:
        r.nome_sala = salas_dict.get(r.id_sala, f"Sala {r.id_sala}")
    return render_template('listar_reservas.html', reservas=reservas, salas=salas)


def form_reserva():
    salas = dados.listar_todas_salas()
    return render_template('criar_reserva.html', salas=salas)


def salvar_reserva():
    id_sala = int(request.form.get('id_sala'))
    data = request.form.get('data')
    hora_inicio_str = request.form.get('hora_inicio')
    duracao_minutos = int(request.form.get('duracao', 60))
    motivo = request.form.get('motivo')
    
    formato = "%H:%M"
    try:
        inicio_dt = datetime.strptime(hora_inicio_str, formato)
        fim_dt = inicio_dt + timedelta(minutes=duracao_minutos)
        hora_fim_str = fim_dt.strftime(formato)
    except Exception:
        hora_fim_str = hora_inicio_str 

    id_reserva = dados.inserir_reserva(id_sala, session['usuario']['id'], data, hora_inicio_str, duracao_minutos, hora_fim_str, motivo)
    
    dados.inserir_notificacao(1, 'Novo Pedido de Reserva', f"Um novo pedido de reserva foi feito para a sala {id_sala} em {data}.")
    dados.inserir_notificacao(2, 'Novo Pedido de Reserva', f"Um novo pedido de reserva foi feito para a sala {id_sala} em {data}.")
    
    return redirect(url_for('listar_reservas'))


def aprovar_reserva():
    id_reserva = request.args.get('id')
    if not id_reserva:
        return redirect(url_for('listar_reservas'))
    
    id_reserva = int(id_reserva)
    reserva = dados.buscar_reserva_por_id(id_reserva)
    if reserva:
        dados.aprovar_reserva_no_banco(id_reserva, session['usuario']['id'])
        dados.inserir_notificacao(reserva.id_professor, 'Mudança de Status', f"Sua reserva para a sala ID {reserva.id_sala} foi aprovada.")
    return redirect(url_for('listar_reservas'))


def form_rejeitar():
    id_reserva = request.args.get('id')
    if not id_reserva:
        return redirect(url_for('listar_reservas'))
        
    id_reserva = int(id_reserva)
    reserva = dados.buscar_reserva_por_id(id_reserva)
    return render_template('rejeitar_reserva.html', reserva=reserva)


def processar_rejeicao():
    id_reserva = int(request.form.get('id_reserva'))
    justificativa = request.form.get('justificativa')
    reserva = dados.buscar_reserva_por_id(id_reserva)
    if reserva:
        dados.rejeitar_reserva_no_banco(id_reserva, session['usuario']['id'], justificativa)
        dados.inserir_notificacao(reserva.id_professor, 'Mudança de Status', f"Sua reserva para a sala ID {reserva.id_sala} foi rejeitada. Motivo: {justificativa}")
    return redirect(url_for('listar_reservas'))


def detalhe_reserva():
    id_reserva = request.args.get('id')
    if not id_reserva:
        return redirect(url_for('listar_reservas'))
        
    id_reserva = int(id_reserva)
    reserva = dados.buscar_reserva_por_id(id_reserva)
    sala = dados.buscar_sala_por_id(reserva.id_sala) if reserva else None
    professor = dados.buscar_usuario_por_id(reserva.id_professor) if reserva else None
    coordenador = dados.buscar_usuario_por_id(reserva.aprovado_por) if reserva and reserva.aprovado_por else None
    return render_template('detalhe_reserva.html', reserva=reserva, sala=sala, professor=professor, coordenador=coordenador)


def liberar_reservas_automatico():
    return redirect(url_for('listar_reservas'))
