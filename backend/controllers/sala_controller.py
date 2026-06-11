from flask import render_template, request, redirect
from models.dados import salas
from controllers.auth_controller import login_required, roles_required

@login_required
def listar_salas():
    return render_template('listar_salas.html', salas=salas)

@login_required
@roles_required('Administrador')
def form_cadastrar_sala():
    return render_template('cadastrar_salas.html')

@login_required
@roles_required('Administrador')
def salvar_sala():
    nome = request.form.get('nome')
    capacidade = request.form.get('capacidade')
    localizacao = request.form.get('localizacao')
    equipamentos = request.form.get('equipamentos')
    
    if nome and capacidade:
        nova_sala = {
            "id": len(salas) + 1,
            "nome": nome, 
            "capacidade": capacidade,
            "localizacao": localizacao,
            "equipamentos": equipamentos if equipamentos else "Nenhum"
        }
        salas.append(nova_sala)
        
    return redirect('/salas')
