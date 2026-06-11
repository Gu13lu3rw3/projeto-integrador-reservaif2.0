from flask import render_template, request, redirect, session
from models.dados import usuarios
from datetime import datetime
from functools import wraps

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
            if 'usuario_perfil' not in session or session.get('usuario_perfil') not in roles:
                return redirect('/dashboard?erro=acesso_negado')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def login():
    return render_template('login.html')

def processar_login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = None
    for u in usuarios:
        if u['email'] == email and u.get('senha') == senha:
            usuario = u
            break

    if usuario:
        session['usuario_id'] = usuario['id']
        session['usuario_nome'] = usuario['nome']
        session['usuario_perfil'] = usuario['perfil']
        session['usuario_email'] = usuario['email']
        session['login_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return redirect('/dashboard')
    else:
        return render_template('login.html', erro='Email ou senha inválidos')

def logout():
    session.clear()
    return redirect('/login')

def dashboard():
    if 'usuario_id' not in session:
        return redirect('/login')

    usuario_info = {
        'id': session.get('usuario_id'),
        'nome': session.get('usuario_nome'),
        'perfil': session.get('usuario_perfil'),
        'email': session.get('usuario_email'),
        'login_timestamp': session.get('login_timestamp')
    }

    return render_template('dashboard.html', usuario=usuario_info)

def verificar_autenticacao():
    return 'usuario_id' in session

def verificar_perfil(perfis_permitidos):
    if 'usuario_perfil' not in session:
        return False

    return session.get('usuario_perfil') in perfis_permitidos

def obter_usuario_sessao():
    if 'usuario_id' not in session:
        return None

    return {
        'id': session.get('usuario_id'),
        'nome': session.get('usuario_nome'),
        'perfil': session.get('usuario_perfil'),
        'email': session.get('usuario_email')
    }
