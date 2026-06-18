from flask import render_template, request, redirect, session
from models.dados import problemas, checklists, salas
from datetime import datetime
from controllers.auth_controller import login_required, roles_required
@login_required
def listar_problemas():
    filtro_status = request.args.get('status', '')
    filtro_sala = request.args.get('id_sala', '')
    problemas_filtrados = problemas
    if filtro_status:
        problemas_filtrados = [p for p in problemas_filtrados if p['status'] == filtro_status]
    if filtro_sala:
        problemas_filtrados = [p for p in problemas_filtrados if str(p['id_sala']) == str(filtro_sala)]
    return render_template(
        'listar_problemas.html',
        problemas=problemas_filtrados,
        salas=salas,
        filtro_status=filtro_status,
        filtro_sala=filtro_sala
    )
@login_required
@roles_required('Professor')
def form_reportar_problema():
    return render_template('reportar_problema.html', salas=salas)
@login_required
@roles_required('Professor')
def salvar_problema():
    id_sala = request.form.get('id_sala')
    descricao = request.form.get('descricao')
    prioridade = request.form.get('prioridade', 'Media')
    id_usuario = session.get('usuario_id')
    if id_sala and descricao:
        novo_problema = {
            "id": len(problemas) + 1,
            "id_sala": id_sala,
            "id_professor": id_usuario,
            "descricao": descricao,
            "prioridade": prioridade,
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Pendente",
            "responsavel": None,
            "data_resolucao": None
        }
        problemas.append(novo_problema)
    return redirect('/problemas')
@login_required
@roles_required('Manutencao')
def atualizar_status_problema():
    id_problema = int(request.args.get('id'))
    novo_status = request.args.get('status')
    id_usuario = session.get('usuario_id')
    status_validos = ['Pendente', 'Em andamento', 'Resolvido']
    if novo_status not in status_validos:
        return redirect('/problemas')
    for p in problemas:
        if p['id'] == id_problema:
            p['status'] = novo_status
            p['responsavel'] = id_usuario
            if novo_status == 'Resolvido':
                p['data_resolucao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for s in salas:
                    if str(s['id']) == str(p['id_sala']):
                        if s.get('status_manutencao') == 'Bloqueada (Manutenção)':
                            s['status_manutencao'] = 'Disponível'
            break
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
    observacoes = request.form.get('observacoes', '')
    status_sala = "Disponível"
    if limpeza == "ruim" or equipamentos == "ruim":
        status_sala = "Bloqueada (Manutenção)"
    novo_checklist = {
        "id": len(checklists) + 1,
        "id_sala": id_sala,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "limpeza": limpeza,
        "equipamentos": equipamentos,
        "observacoes": observacoes,
        "status": status_sala
    }
    checklists.append(novo_checklist)
    for s in salas:
        if str(s['id']) == id_sala:
            s['status_manutencao'] = status_sala
    return redirect('/salas')
