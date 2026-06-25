from flask import render_template, request
from datetime import datetime
from models import dados


def form_consulta():
    salas = dados.listar_todas_salas()
    return render_template('consultar_disponibilidade.html', salas=salas)


def filtrar():
    data = request.form.get('data')
    hora_inicio = request.form.get('hora_inicio')
    hora_fim = request.form.get('hora_fim')
    id_sala = request.form.get('id_sala')

    todas_salas = dados.listar_todas_salas()
    salas_disponiveis = []

    if id_sala:
        sala = dados.buscar_sala_por_id(int(id_sala))
        if sala and verifica_disponibilidade(sala.id, data, hora_inicio, hora_fim):
            salas_disponiveis.append(sala)
    else:
        for sala in todas_salas:
            if verifica_disponibilidade(sala.id, data, hora_inicio, hora_fim):
                salas_disponiveis.append(sala)

    return render_template(
        'resultado_disponibilidade.html',
        salas=salas_disponiveis,
        data=data,
        hora_inicio=hora_inicio,
        hora_fim=hora_fim,
        todas_salas=todas_salas
    )


def verifica_disponibilidade(id_sala, data, hora_inicio, hora_fim):
    try:
        inicio_minutos = converter_hora_para_minutos(hora_inicio)
        fim_minutos = converter_hora_para_minutos(hora_fim)

        reservas_da_sala = dados.listar_reservas_da_sala_na_data(id_sala, data)
        for reserva in reservas_da_sala:
            if reserva.status not in ["Rejeitada", "Concluída (Liberada)"]:
                reserva_inicio = converter_hora_para_minutos(reserva.hora_inicio)
                reserva_fim = converter_hora_para_minutos(reserva.hora_fim)
                if inicio_minutos < reserva_fim and fim_minutos > reserva_inicio:
                    return False

        data_obj = datetime.strptime(data, "%Y-%m-%d")
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        dia_semana = dias_semana[data_obj.weekday()]

        horarios = dados.listar_horarios_oficiais_da_sala(id_sala, dia_semana)
        for horario in horarios:
            horario_inicio = converter_hora_para_minutos(str(horario['hora_inicio']))
            horario_fim = converter_hora_para_minutos(str(horario['hora_fim']))
            if inicio_minutos < horario_fim and fim_minutos > horario_inicio:
                return False

        return True
    except:
        return False


def converter_hora_para_minutos(hora_str):
    try:
        partes = hora_str.split(':')
        hora = int(partes[0])
        minuto = int(partes[1])
        return hora * 60 + minuto
    except:
        return 0
