from flask import render_template, request, redirect, url_for, session
from models import dados


def listar_problemas():
    status_filtro = request.args.get('status')
    sala_filtro = request.args.get('id_sala')
    salas = dados.listar_todas_salas()
    lista = dados.listar_todos_problemas()
    
    if status_filtro:
        lista = [p for p in lista if p.status == status_filtro]
    if sala_filtro:
        lista = [p for p in lista if str(p.id_sala) == str(sala_filtro)]
        
    return render_template('listar_problemas.html', problemas=lista, salas=salas)


def form_problema():
    salas = dados.listar_todas_salas()
    return render_template('reportar_problema.html', salas=salas)


def salvar_problema():
    id_sala = int(request.form.get('id_sala'))
    descricao = request.form.get('descricao')
    prioridade = request.form.get('prioridade')
    
    dados.inserir_problema(id_sala, descricao, prioridade, session['usuario']['id'])
    
    if prioridade == "Alta":
        dados.atualizar_status_sala(id_sala, "Bloqueada (Manutenção)")
        dados.inserir_notificacao(1, 'Sala Bloqueada', f"A sala {id_sala} foi bloqueada automaticamente devido a um problema de alta gravidade.")
        
    return redirect(url_for('listar_problemas'))


def atualizar_status_problema():
    id_problema = request.args.get('id')
    novo_status = request.args.get('status')
    
    if not id_problema or not novo_status:
        return redirect(url_for('listar_problemas'))
        
    id_problema = int(id_problema)
    problema = dados.buscar_problema_por_id(id_problema)
    
    if problema:
        dados.atualizar_status_problema_no_banco(id_problema, novo_status, session['usuario']['id'])
        
        if novo_status == "Resolvido":
            sala = dados.buscar_sala_por_id(problema.id_sala)
            outros_pendentes = dados.contar_problemas_pendentes_alta_prioridade(problema.id_sala)
            
            if sala and outros_pendentes == 0:
                dados.atualizar_status_sala(problema.id_sala, "Disponível")
            
            dados.inserir_notificacao(problema.reportado_por, 'Mudança de Status', f"O problema reportado na sala {sala.nome if sala else problema.id_sala} foi resolvido.")
            
    return redirect(url_for('listar_problemas'))


def form_checklist():
    salas = dados.listar_todas_salas()
    return render_template('realizar_checklist.html', salas=salas)


def salvar_checklist():
    id_sala = request.form.get('id_sala')
    if id_sala:
        dados.inserir_checklist(int(id_sala), session['usuario']['id'])
    return redirect(url_for('dashboard'))
