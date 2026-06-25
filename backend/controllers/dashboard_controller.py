from flask import render_template, send_file
from models import dados
import csv
import io
from datetime import datetime


def exibir_indicadores():
    salas = dados.listar_todas_salas()
    reservas = dados.listar_todas_reservas()
    problemas = dados.listar_todos_problemas()

    total_salas = len(salas)
    salas_disponiveis = len([s for s in salas if s.status == "Disponível"])
    salas_bloqueadas = len([s for s in salas if s.status == "Bloqueada (Manutenção)"])
    total_reservas = len(reservas)
    reservas_pendentes = len([r for r in reservas if r.status == "Pendente"])
    reservas_aprovadas = len([r for r in reservas if r.status == "Aprovada"])
    reservas_rejeitadas = len([r for r in reservas if r.status == "Rejeitada"])
    reservas_concluidas = len([r for r in reservas if r.status == "Concluída"])
    taxa_aprovacao = round((reservas_aprovadas / total_reservas * 100), 1) if total_reservas > 0 else 0
    problemas_pendentes = len([p for p in problemas if p.status == "Pendente"])
    problemas_andamento = len([p for p in problemas if p.status == "Em andamento"])
    problemas_resolvidos = len([p for p in problemas if p.status == "Resolvido"])

    reservas_por_sala = []
    for s in salas:
        count = len([r for r in reservas if r.id_sala == s.id])
        reservas_por_sala.append({"nome": s.nome, "total": count})

    return render_template('dashboard_indicadores.html',
        total_salas=total_salas, salas_disponiveis=salas_disponiveis, salas_bloqueadas=salas_bloqueadas,
        total_reservas=total_reservas, reservas_pendentes=reservas_pendentes,
        reservas_aprovadas=reservas_aprovadas, reservas_rejeitadas=reservas_rejeitadas,
        reservas_concluidas=reservas_concluidas, taxa_aprovacao=taxa_aprovacao,
        problemas_pendentes=problemas_pendentes, problemas_andamento=problemas_andamento,
        problemas_resolvidos=problemas_resolvidos, tempo_medio_reparo=dados.calcular_tmr(),
        reservas_por_sala=reservas_por_sala)


def relatorios():
    salas = dados.listar_todas_salas()
    reservas = dados.listar_todas_reservas()
    problemas = dados.listar_todos_problemas()

    uso_por_sala = []
    for s in salas:
        res_sala = [r for r in reservas if r.id_sala == s.id]
        uso_por_sala.append({
            'nome': s.nome, 'localizacao': s.localizacao, 'capacidade': s.capacidade,
            'total_reservas': len(res_sala),
            'aprovadas': len([r for r in res_sala if r.status == 'Aprovada']),
            'rejeitadas': len([r for r in res_sala if r.status == 'Rejeitada']),
            'problemas': len([p for p in problemas if p.id_sala == s.id]),
            'status': s.status
        })
    return render_template('relatorios.html',
        uso_por_sala=uso_por_sala, total_reservas=len(reservas),
        total_aprovadas=len([r for r in reservas if r.status == 'Aprovada']),
        total_rejeitadas=len([r for r in reservas if r.status == 'Rejeitada']),
        total_problemas=len(problemas),
        total_resolvidos=len([p for p in problemas if p.status == 'Resolvido']),
        data_geracao=datetime.now().strftime("%d/%m/%Y %H:%M"))


def exportar_relatorio_csv():
    salas = dados.listar_todas_salas()
    reservas = dados.listar_todas_reservas()
    problemas = dados.listar_todos_problemas()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Relatório Estratégico de Uso das Salas'])
    writer.writerow(['Gerado em', datetime.now().strftime("%d/%m/%Y %H:%M")])
    writer.writerow([])
    writer.writerow(['SALA', 'LOCALIZAÇÃO', 'CAPACIDADE', 'TOTAL RESERVAS', 'APROVADAS', 'REJEITADAS', 'PROBLEMAS', 'STATUS'])
    for s in salas:
        res_sala = [r for r in reservas if r.id_sala == s.id]
        writer.writerow([
            s.nome, s.localizacao, s.capacidade, len(res_sala),
            len([r for r in res_sala if r.status == 'Aprovada']),
            len([r for r in res_sala if r.status == 'Rejeitada']),
            len([p for p in problemas if p.id_sala == s.id]),
            s.status
        ])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode('utf-8-sig')),
                     mimetype='text/csv', as_attachment=True,
                     download_name=f'relatorio_reservaif_{datetime.now().strftime("%Y%m%d")}.csv')
