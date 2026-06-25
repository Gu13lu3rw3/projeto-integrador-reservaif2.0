from flask import jsonify
from models import dados

def get_salas():
    salas = dados.listar_todas_salas()
    lista_salas = []
    for s in salas:
        lista_salas.append({
            'id': s.id,
            'nome': s.nome,
            'capacidade': s.capacidade,
            'localizacao': s.localizacao,
            'status': s.status_manutencao
        })
    return jsonify(lista_salas)

def get_estatisticas():
    salas = dados.listar_todas_salas()
    reservas = dados.listar_todas_reservas()
    problemas = dados.listar_todos_problemas()
    
    stats = {
        'total_salas': len(salas),
        'total_reservas': len(reservas),
        'problemas_ativos': len([p for p in problemas if p.status != 'Resolvido']),
        'sistema': 'ReservaIF 2.0',
        'status': 'Online'
    }
    return jsonify(stats)
