from flask import render_template, request
from models.dados import salas, reservas, horarios_oficiais
from datetime import datetime

def consultar_disponibilidade():
    return render_template('consultar_disponibilidade.html', salas=salas)

def filtrar_disponibilidade():
    data = request.form.get('data')
    hora_inicio = request.form.get('hora_inicio')
    hora_fim = request.form.get('hora_fim')
    id_sala = request.form.get('id_sala')

    salas_disponiveis = []

    if id_sala:
        sala = next((s for s in salas if str(s['id']) == str(id_sala)), None)
        if sala:
            if verifica_disponibilidade(sala['id'], data, hora_inicio, hora_fim):
                salas_disponiveis.append(sala)
    else:
        for sala in salas:
            if verifica_disponibilidade(sala['id'], data, hora_inicio, hora_fim):
                salas_disponiveis.append(sala)

    return render_template(
        'resultado_disponibilidade.html',
        salas=salas_disponiveis,
        data=data,
        hora_inicio=hora_inicio,
        hora_fim=hora_fim,
        todas_salas=salas
    )

def verifica_disponibilidade(id_sala, data, hora_inicio, hora_fim):
    try:
        inicio_minutos = converter_hora_para_minutos(hora_inicio)
        fim_minutos = converter_hora_para_minutos(hora_fim)

        for reserva in reservas:
            if str(reserva['id_sala']) == str(id_sala) and reserva['data'] == data:
                if reserva['status'] not in ["Rejeitada", "Concluída (Liberada)"]:
                    reserva_inicio = converter_hora_para_minutos(reserva['hora_inicio'])
                    reserva_fim = converter_hora_para_minutos(reserva['hora_fim'])
                    if inicio_minutos < reserva_fim and fim_minutos > reserva_inicio:
                        return False

        data_obj = datetime.strptime(data, "%Y-%m-%d")
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dia_semana = dias_semana[data_obj.weekday()]

        for horario in horarios_oficiais:
            if str(horario['id_sala']) == str(id_sala) and horario['dia_semana'] == dia_semana:
                horario_inicio = converter_hora_para_minutos(horario['hora_inicio'])
                horario_fim = converter_hora_para_minutos(horario['hora_fim'])
                if inicio_minutos < horario_fim and fim_minutos > horario_inicio:
                    return False

        return True
    except:
        return False

def converter_hora_para_minutos(hora_str):
    try:
        hora, minuto = map(int, hora_str.split(':'))
        return hora * 60 + minuto
    except:
        return 0
