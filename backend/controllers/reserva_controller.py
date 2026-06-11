from flask import render_template, request, redirect, session
from models.dados import reservas, salas, notificacoes, horarios_oficiais
from controllers.notificacao_controller import criar_notificacao_pedido, criar_notificacao_status
from controllers.auth_controller import login_required, roles_required
from datetime import datetime, timedelta

@login_required
def listar_reservas():
    return render_template('listar_reservas.html', reservas=reservas)

@login_required
@roles_required('Professor')
def form_criar_reserva():
    return render_template('criar_reserva.html', salas=salas)

@login_required
@roles_required('Professor')
def salvar_reserva():
    id_sala = request.form.get('id_sala')
    data = request.form.get('data')
    hora_inicio = request.form.get('hora_inicio')
    duracao = request.form.get('duracao')
    motivo = request.form.get('motivo')

    id_professor = session.get('usuario_id')

    if id_sala and data and hora_inicio and duracao:
        inicio = datetime.strptime(hora_inicio, "%H:%M")
        fim = inicio + timedelta(minutes=int(duracao))
        hora_fim = fim.strftime("%H:%M")

        if verifica_conflito_horario_oficial(id_sala, data, hora_inicio, hora_fim):
            return redirect('/reservas?erro=conflito_horario')

        nova_reserva = {
            "id": len(reservas) + 1,
            "id_sala": id_sala,
            "id_professor": id_professor,
            "data": data,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "motivo": motivo,
            "status": "Pendente"
        }
        reservas.append(nova_reserva)

        criar_notificacao_pedido(nova_reserva['id'], id_professor, id_sala, motivo)

    return redirect('/reservas')

@login_required
@roles_required('Coordenador')
def aprovar_reserva():
    id_reserva = int(request.args.get('id'))
    for r in reservas:
        if r['id'] == id_reserva:
            r['status'] = "Aprovada"
            criar_notificacao_status(r['id_professor'], f"Sua reserva #{id_reserva} foi APROVADA.")
    return redirect('/reservas')

@login_required
@roles_required('Coordenador')
def rejeitar_reserva():
    id_reserva = int(request.args.get('id'))
    for r in reservas:
        if r['id'] == id_reserva:
            r['status'] = "Rejeitada"
            criar_notificacao_status(r['id_professor'], f"Sua reserva #{id_reserva} foi REJEITADA.")
    return redirect('/reservas')

@login_required
def liberar_sala_automatica():
    agora = datetime.now()
    data_atual = agora.strftime("%Y-%m-%d")
    hora_atual = agora.strftime("%H:%M")
    
    for r in reservas:
        if r['status'] == "Aprovada":
            if r['data'] < data_atual or (r['data'] == data_atual and r['hora_fim'] <= hora_atual):
                r['status'] = "Concluída (Liberada)"
                
    return redirect('/reservas')

def verifica_conflito_horario_oficial(id_sala, data, hora_inicio, hora_fim):
    try:
        data_obj = datetime.strptime(data, "%Y-%m-%d")
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dia_semana = dias_semana[data_obj.weekday()]

        inicio_minutos = converter_hora_para_minutos(hora_inicio)
        fim_minutos = converter_hora_para_minutos(hora_fim)

        for horario in horarios_oficiais:
            if str(horario['id_sala']) == str(id_sala) and horario['dia_semana'] == dia_semana:
                horario_inicio = converter_hora_para_minutos(horario['hora_inicio'])
                horario_fim = converter_hora_para_minutos(horario['hora_fim'])

                if inicio_minutos < horario_fim and fim_minutos > horario_inicio:
                    return True

        return False
    except:
        return False

def converter_hora_para_minutos(hora_str):
    try:
        hora, minuto = map(int, hora_str.split(':'))
        return hora * 60 + minuto
    except:
        return 0
