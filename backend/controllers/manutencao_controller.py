from flask import render_template, request, redirect, session
from models.dados import problemas, checklists, salas
from datetime import datetime
from controllers.auth_controller import login_required, roles_required

@login_required
def listar_problemas():
    return render_template('listar_problemas.html', problemas=problemas)

@login_required
@roles_required('Professor')
def form_reportar_problema():
    return render_template('reportar_problema.html', salas=salas)

@login_required
@roles_required('Professor')
def salvar_problema():
    id_sala = request.form.get('id_sala')
    descricao = request.form.get('descricao')
    id_usuario = session.get('usuario_id')
    
    if id_sala and descricao:
        novo_problema = {
            "id": len(problemas) + 1,
            "id_sala": id_sala,
            "id_professor": id_usuario,
            "descricao": descricao,
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Pendente"
        }
        problemas.append(novo_problema)
    return redirect('/problemas')

@login_required
@roles_required('Manutencao')
def form_checklist():
    return render_template('realizar_checklist.html', salas=salas)

@login_required
@roles_required('Manutencao')
def salvar_checklist():
    id_sala = request.form.get('id_sala')
    limpeza = request.form.get('limpeza')
    equipamentos = request.form.get('equipamentos')
    
    status_sala = "Disponível"
    if limpeza == "ruim" or equipamentos == "ruim":
        status_sala = "Bloqueada (Manutenção)"
        
    novo_checklist = {
        "id": len(checklists) + 1,
        "id_sala": id_sala,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": status_sala
    }
    checklists.append(novo_checklist)
    
    for s in salas:
        if str(s['id']) == id_sala:
            s['status_manutencao'] = status_sala
            
    return redirect('/salas')
