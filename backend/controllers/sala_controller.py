from flask import render_template, request, redirect, url_for
from models import dados


def listar_salas():
    salas = dados.listar_todas_salas()
    return render_template('listar_salas.html', salas=salas)


def form_sala():
    return render_template('cadastrar_salas.html')


def salvar_sala():
    nome = request.form.get('nome')
    capacidade = request.form.get('capacidade')
    localizacao = request.form.get('localizacao')
    if nome and capacidade:
        dados.inserir_sala(nome, capacidade, localizacao)
    return redirect(url_for('listar_salas'))
