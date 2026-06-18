from flask import render_template, request, redirect, session
from functools import wraps
from datetime import datetime
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            perfil = session.get('usuario_perfil')
            if perfil not in roles:
                return render_template('acesso_negado.html', perfil=perfil, roles_necessarios=roles)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
def login():
    erro = request.args.get('erro')
    return render_template('login.html', erro=erro)
def processar_login():
    from models.dados import usuarios
    email = request.form.get('email')
    senha = request.form.get('senha')
    usuario = next((u for u in usuarios if u['email'] == email and u['senha'] == senha), None)
    if usuario:
        session['usuario_id'] = usuario['id']
        session['usuario_nome'] = usuario['nome']
        session['usuario_perfil'] = usuario['perfil']
        session['usuario_email'] = usuario['email']
        return redirect('/dashboard')
    else:
        return redirect('/login?erro=credenciais_invalidas')
def logout():
    session.clear()
    return redirect('/login')
@login_required
def dashboard():
    from models.dados import usuarios
    usuario = next((u for u in usuarios if u['id'] == session['usuario_id']), None)
    if usuario:
        usuario['login_timestamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template('dashboard.html', usuario=usuario)
def form_recuperar_senha():
    mensagem = request.args.get('mensagem')
    erro = request.args.get('erro')
    return render_template('recuperar_senha.html', mensagem=mensagem, erro=erro)
def processar_recuperacao_senha():
    from models.dados import usuarios
    email = request.form.get('email')
    usuario = next((u for u in usuarios if u['email'] == email), None)
    if usuario:
        return redirect(f'/recuperar_senha/confirmar?email={email}')
    else:
        return redirect('/recuperar_senha?erro=email_nao_encontrado')
def confirmar_recuperacao_senha():
    from models.dados import usuarios
    email = request.args.get('email')
    usuario = next((u for u in usuarios if u['email'] == email), None)
    if not usuario:
        return redirect('/recuperar_senha?erro=email_nao_encontrado')
    return render_template('confirmar_recuperacao.html', usuario=usuario)
