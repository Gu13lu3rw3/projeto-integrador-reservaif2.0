from flask import render_template, make_response
from models.dados import reservas, salas, problemas, checklists
from controllers.auth_controller import login_required, roles_required
from datetime import datetime
import csv
import io
@login_required
@roles_required('Coordenador', 'Administrador')
def dashboard_indicadores():
    total_salas = len(salas)
    total_reservas = len(reservas)
    reservas_pendentes = sum(1 for r in reservas if r['status'] == 'Pendente')
    reservas_aprovadas = sum(1 for r in reservas if r['status'] == 'Aprovada')
    reservas_rejeitadas = sum(1 for r in reservas if r['status'] == 'Rejeitada')
    reservas_concluidas = sum(1 for r in reservas if r['status'] == 'Concluída (Liberada)')
    salas_bloqueadas = sum(1 for s in salas if s.get('status_manutencao') == 'Bloqueada (Manutenção)')
    salas_disponiveis = total_salas - salas_bloqueadas
    problemas_pendentes = sum(1 for p in problemas if p['status'] == 'Pendente')
    problemas_andamento = sum(1 for p in problemas if p['status'] == 'Em andamento')
    problemas_resolvidos = sum(1 for p in problemas if p['status'] == 'Resolvido')
    reservas_por_sala = []
    for sala in salas:
        qtd = sum(1 for r in reservas if str(r['id_sala']) == str(sala['id']))
        reservas_por_sala.append({"nome": sala['nome'], "total": qtd})
    total_decididas = reservas_aprovadas + reservas_rejeitadas
    taxa_aprovacao = round((reservas_aprovadas / total_decididas * 100), 1) if total_decididas > 0 else 0
    tempos = []
    for p in problemas:
        if p['status'] == 'Resolvido' and p.get('data_resolucao'):
            try:
                inicio = datetime.strptime(p['data_hora'], "%Y-%m-%d %H:%M:%S")
                fim = datetime.strptime(p['data_resolucao'], "%Y-%m-%d %H:%M:%S")
                delta_horas = (fim - inicio).total_seconds() / 3600
                tempos.append(delta_horas)
            except:
                pass
    tempo_medio_reparo = round(sum(tempos) / len(tempos), 1) if tempos else 0
    return render_template(
        'dashboard_indicadores.html',
        total_salas=total_salas,
        total_reservas=total_reservas,
        reservas_pendentes=reservas_pendentes,
        reservas_aprovadas=reservas_aprovadas,
        reservas_rejeitadas=reservas_rejeitadas,
        reservas_concluidas=reservas_concluidas,
        salas_bloqueadas=salas_bloqueadas,
        salas_disponiveis=salas_disponiveis,
        problemas_pendentes=problemas_pendentes,
        problemas_andamento=problemas_andamento,
        problemas_resolvidos=problemas_resolvidos,
        reservas_por_sala=reservas_por_sala,
        taxa_aprovacao=taxa_aprovacao,
        tempo_medio_reparo=tempo_medio_reparo
    )
@login_required
@roles_required('Administrador')
def relatorios():
    uso_por_sala = []
    for sala in salas:
        reservas_sala = [r for r in reservas if str(r['id_sala']) == str(sala['id'])]
        total = len(reservas_sala)
        aprovadas = sum(1 for r in reservas_sala if r['status'] in ['Aprovada', 'Concluída (Liberada)'])
        rejeitadas = sum(1 for r in reservas_sala if r['status'] == 'Rejeitada')
        problemas_sala = sum(1 for p in problemas if str(p['id_sala']) == str(sala['id']))
        uso_por_sala.append({
            "id": sala['id'],
            "nome": sala['nome'],
            "localizacao": sala.get('localizacao', '-'),
            "capacidade": sala.get('capacidade', '-'),
            "total_reservas": total,
            "aprovadas": aprovadas,
            "rejeitadas": rejeitadas,
            "problemas": problemas_sala,
            "status": sala.get('status_manutencao', 'Disponível')
        })
    total_reservas = len(reservas)
    total_aprovadas = sum(1 for r in reservas if r['status'] in ['Aprovada', 'Concluída (Liberada)'])
    total_rejeitadas = sum(1 for r in reservas if r['status'] == 'Rejeitada')
    total_problemas = len(problemas)
    total_resolvidos = sum(1 for p in problemas if p['status'] == 'Resolvido')
    return render_template(
        'relatorios.html',
        uso_por_sala=uso_por_sala,
        total_reservas=total_reservas,
        total_aprovadas=total_aprovadas,
        total_rejeitadas=total_rejeitadas,
        total_problemas=total_problemas,
        total_resolvidos=total_resolvidos,
        data_geracao=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )
@login_required
@roles_required('Administrador')
def exportar_relatorio_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Relatório de Uso de Salas - ReservaIF 2.0'])
    writer.writerow(['Gerado em:', datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    writer.writerow([])
    writer.writerow(['Sala', 'Localização', 'Capacidade', 'Total Reservas', 'Aprovadas', 'Rejeitadas', 'Problemas Reportados', 'Status'])
    for sala in salas:
        reservas_sala = [r for r in reservas if str(r['id_sala']) == str(sala['id'])]
        total = len(reservas_sala)
        aprovadas = sum(1 for r in reservas_sala if r['status'] in ['Aprovada', 'Concluída (Liberada)'])
        rejeitadas = sum(1 for r in reservas_sala if r['status'] == 'Rejeitada')
        problemas_sala = sum(1 for p in problemas if str(p['id_sala']) == str(sala['id']))
        writer.writerow([
            sala['nome'],
            sala.get('localizacao', '-'),
            sala.get('capacidade', '-'),
            total,
            aprovadas,
            rejeitadas,
            problemas_sala,
            sala.get('status_manutencao', 'Disponível')
        ])
    writer.writerow([])
    writer.writerow(['Reservas Detalhadas'])
    writer.writerow(['ID', 'Sala ID', 'Data', 'Início', 'Fim', 'Motivo', 'Status', 'Criada em'])
    for r in reservas:
        writer.writerow([
            r['id'],
            r['id_sala'],
            r['data'],
            r['hora_inicio'],
            r['hora_fim'],
            r.get('motivo', '-'),
            r['status'],
            r.get('data_criacao', '-')
        ])
    output.seek(0)
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=relatorio_reservaif.csv'
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'
    return response
