from flask import render_template, request, redirect
from models.dados import problemas, checklists, salas

def listar_problemas():
    return render_template('listar_problemas.html', problemas=problemas)

def form_reportar_problema():
    return render_template('reportar_problema.html', salas=salas)

def salvar_problema():
    id_sala = request.form.get('id_sala')
    descricao = request.form.get('descricao')
    
    if id_sala and descricao:
        novo_problema = {
            "id": len(problemas) + 1,
            "id_sala": id_sala,
            "descricao": descricao,
            "status": "Pendente"
        }
        problemas.append(novo_problema)
    return redirect('/problemas')

def form_checklist():
    return render_template('realizar_checklist.html', salas=salas)

def salvar_checklist():
    id_sala = request.form.get('id_sala')
    limpeza = request.form.get('limpeza')
    equipamentos = request.form.get('equipamentos')
    
    status_sala = "Disponível"
    if limpeza == "ruim" or equipamentos == "ruim":
        status_sala = "Bloqueada (Manutenção)"
        
    novo_checklist = {
        "id_sala": id_sala,
        "status": status_sala
    }
    checklists.append(novo_checklist)
    
    # Atualiza status da sala
    for s in salas:
        if str(s['id']) == id_sala:
            s['status_manutencao'] = status_sala
            
    return redirect('/salas')
