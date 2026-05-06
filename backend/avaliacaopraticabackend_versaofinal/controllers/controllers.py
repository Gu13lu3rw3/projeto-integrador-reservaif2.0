from flask import render_template, request, redirect, url_for
import random
from models.questao import Questao

# aqui eu simulei um banco de dados usando uma lista em memória
questoes_db = [
    Questao(0, 'Qual é a capital do Brasil?', 'São Paulo', 'Brasília', 'Rio de Janeiro', 'b'),
    Questao(1, 'Qual é o maior planeta do sistema solar?', 'Saturno', 'Marte', 'Júpiter', 'c'),
    Questao(2, 'Em que ano o Brasil foi descoberto?', '1500', '1492', '1530', 'a')
]

# aqui eu guardo a pontuação do jogador enquanto o servidor tá rodando
contador = {'respondidas': 0, 'acertos': 0, 'erros': 0}

# --- funções do jogo ---

def index():
    # renderiza a página inicial com o menu
    return render_template('index.html')

def jogo():
    # aqui eu sorteio uma pergunta aleatória da minha lista
    if not questoes_db:
        return "nenhuma questão cadastrada.", 404
    questao = random.choice(questoes_db)
    return render_template('jogo.html', questao=questao.to_dict(), questao_id=questao.id, 
                           respondidas=contador['respondidas'], acertos=contador['acertos'], erros=contador['erros'])

def responder():
    # aqui eu pego a resposta que veio do formulário e verifico se tá certa
    questao_id = int(request.form.get('questao_id'))
    resposta_usuario = request.form.get('resposta')
    questao = next((q for q in questoes_db if q.id == questao_id), None)
    
    acertou = resposta_usuario == questao.resposta
    contador['respondidas'] += 1
    if acertou:
        contador['acertos'] += 1
    else:
        contador['erros'] += 1
    
    return render_template('resultado.html', questao=questao.to_dict(), resposta_usuario=resposta_usuario, 
                           acertou=acertou, respondidas=contador['respondidas'], acertos=contador['acertos'], erros=contador['erros'])

def resetar():
    # zera os contadores e volta pro início
    contador['respondidas'] = 0
    contador['acertos'] = 0
    contador['erros'] = 0
    return redirect(url_for('index'))

# --- funções de administração (crud) ---

def admin_listar():
    # mostra a tabela com todas as questões
    return render_template('admin.html', questoes=questoes_db)

def admin_nova():
    # abre o formulário para criar uma nova questão
    return render_template('admin_form.html', questao=None)

def admin_salvar():
    # aqui eu recebo os dados do formulário e salvo na lista (criação ou edição)
    id_str = request.form.get('id')
    pergunta = request.form.get('pergunta')
    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('c')
    resposta = request.form.get('resposta')
    
    if id_str: # se tem id, eu estou editando uma que já existe
        idx = int(id_str)
        questao = next((q for q in questoes_db if q.id == idx), None)
        if questao:
            questao.pergunta = pergunta
            questao.a = a
            questao.b = b
            questao.c = c
            questao.resposta = resposta
    else: # se não tem id, eu crio uma nova e dou um id pra ela
        novo_id = max([q.id for q in questoes_db], default=-1) + 1
        nova_q = Questao(novo_id, pergunta, a, b, c, resposta)
        questoes_db.append(nova_q)
    return redirect(url_for('admin_listar'))

def admin_editar(id):
    # busca a questão pelo id para preencher o formulário de edição
    questao = next((q for q in questoes_db if q.id == id), None)
    return render_template('admin_form.html', questao=questao)

def admin_excluir(id):
    # remove a questão da lista
    global questoes_db
    questoes_db = [q for q in questoes_db if q.id != id]
    return redirect(url_for('admin_listar'))
