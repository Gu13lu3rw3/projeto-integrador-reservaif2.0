from flask import render_template, request, redirect
from models.dados import reservas, salas, notificacoes
from datetime import datetime, timedelta

def listar_reservas():
    return render_template('listar_reservas.html', reservas=reservas)

def form_criar_reserva():
    return render_template('criar_reserva.html', salas=salas)

def salvar_reserva():
    id_sala = request.form.get('id_sala')
    data = request.form.get('data')
    hora_inicio = request.form.get('hora_inicio')
    duracao = request.form.get('duracao')
    motivo = request.form.get('motivo')
    
    if id_sala and data and hora_inicio and duracao:
        # HU02: Cálculo automático de término
        inicio = datetime.strptime(hora_inicio, "%H:%M")
        fim = inicio + timedelta(minutes=int(duracao))
        hora_fim = fim.strftime("%H:%M")
        
        nova_reserva = {
            "id": len(reservas) + 1,
            "id_sala": id_sala,
            "data": data,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "motivo": motivo,
            "status": "Pendente" # HU04: Começa pendente
        }
        reservas.append(nova_reserva)
        
    return redirect('/reservas')

def aprovar_reserva():
    id_reserva = int(request.args.get('id'))
    for r in reservas:
        if r['id'] == id_reserva:
            r['status'] = "Aprovada"
            # HU09: Simulação de notificação de mudança de status
            notificacoes.append({
                "mensagem": f"Sua reserva {id_reserva} foi APROVADA.",
                "lida": False
            })
    return redirect('/reservas')

def rejeitar_reserva():
    id_reserva = int(request.args.get('id'))
    for r in reservas:
        if r['id'] == id_reserva:
            r['status'] = "Rejeitada"
            # HU09: Simulação de notificação de mudança de status
            notificacoes.append({
                "mensagem": f"Sua reserva {id_reserva} foi REJEITADA.",
                "lida": False
            })
    return redirect('/reservas')

def liberar_sala_automatica():
    # HU11: Simulação de liberação automática
    # Na vida real isso seria um cron job, aqui apenas limpamos status
    for r in reservas:
        if r['status'] == "Aprovada":
            r['status'] = "Concluída (Liberada)"
    return redirect('/reservas')
