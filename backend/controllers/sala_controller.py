from flask import render_template, request, redirect
from models.dados import salas

def listar_salas():
    return render_template('listar_salas.html', salas=salas)

def form_cadastrar_sala():
    return render_template('cadastrar_salas.html')

def salvar_sala():
    nome = request.form.get('nome')
    capacidade = request.form.get('capacidade')
    localizacao = request.form.get('localizacao')
    
    if nome and capacidade:
        nova_sala = {
            "id": len(salas) + 1,
            "nome": nome, 
            "capacidade": capacidade,
            "localizacao": localizacao
        }
        salas.append(nova_sala)
        
    return redirect('/salas')
