
from flask import render_template, request, redirect, url_for, session, send_file
from functools import wraps
from controllers import (
    sala_controller, reserva_controller, auth_controller, 
    notificacao_controller, manutencao_controller, disponibilidade_controller,
    dashboard_controller
)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session or session['usuario']['perfil'] != 'Administrador':
            return render_template('acesso_negado.html', perfil=session['usuario']['perfil'] if 'usuario' in session else 'Nenhum')
        return f(*args, **kwargs)
    return decorated_function
def adicionar_rotas(app):
    @app.route('/')
    def index():
        return redirect(url_for('login'))
    @app.route('/login')
    def login():
        return auth_controller.form_login()
    @app.route('/processar_login', methods=['POST'])
    def processar_login():
        return auth_controller.processar_login()
    @app.route('/logout')
    def logout():
        return auth_controller.logout()
    @app.route('/recuperar_senha')
    def recuperar_senha():
        return auth_controller.form_recuperar_senha()
    @app.route('/recuperar_senha/processar', methods=['POST'])
    def processar_recuperacao():
        return auth_controller.processar_recuperacao_senha()
    @app.route('/recuperar_senha/confirmar')
    def confirmar_recuperacao():
        return auth_controller.confirmar_recuperacao()
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return auth_controller.dashboard()
    @app.route('/dashboard/indicadores')
    @login_required
    def dashboard_indicadores():
        if session['usuario']['perfil'] not in ['Coordenador', 'Administrador']:
            return render_template('acesso_negado.html', perfil=session['usuario']['perfil'])
        return dashboard_controller.exibir_indicadores()
    @app.route('/relatorios')
    @admin_required
    def relatorios():
        return dashboard_controller.relatorios()
    @app.route('/relatorios/exportar')
    @admin_required
    def exportar_relatorio():
        return dashboard_controller.exportar_relatorio_csv()
    @app.route('/salas')
    @login_required
    def listar_salas():
        return sala_controller.listar_salas()
    @app.route('/salas/novo')
    @admin_required
    def form_sala():
        return sala_controller.form_sala()
    @app.route('/salas/salvar', methods=['POST'])
    @admin_required
    def salvar_sala():
        return sala_controller.salvar_sala()
    @app.route('/reservas')
    @login_required
    def listar_reservas():
        return reserva_controller.listar_reservas()
    @app.route('/reservas/novo')
    @login_required
    def form_reserva():
        return reserva_controller.form_reserva()
    @app.route('/reservas/salvar', methods=['POST'])
    @login_required
    def salvar_reserva():
        return reserva_controller.salvar_reserva()
    @app.route('/reservas/aprovar')
    @login_required
    def aprovar_reserva():
        return reserva_controller.aprovar_reserva()
    @app.route('/reservas/rejeitar/form')
    @login_required
    def form_rejeitar():
        return reserva_controller.form_rejeitar()
    @app.route('/reservas/rejeitar/processar', methods=['POST'])
    @login_required
    def processar_rejeicao():
        return reserva_controller.processar_rejeicao()
    @app.route('/reservas/detalhe')
    @login_required
    def detalhe_reserva():
        return reserva_controller.detalhe_reserva()
    @app.route('/reservas/liberar')
    @login_required
    def liberar_reservas():
        return reserva_controller.liberar_reservas_automatico()
    @app.route('/disponibilidade')
    @login_required
    def consultar_disponibilidade():
        return disponibilidade_controller.form_consulta()
    @app.route('/disponibilidade/filtrar', methods=['POST'])
    @login_required
    def filtrar_disponibilidade():
        return disponibilidade_controller.filtrar()
    @app.route('/problemas')
    @login_required
    def listar_problemas():
        return manutencao_controller.listar_problemas()
    @app.route('/problemas/novo')
    @login_required
    def form_problema():
        return manutencao_controller.form_problema()
    @app.route('/problemas/salvar', methods=['POST'])
    @login_required
    def salvar_problema():
        return manutencao_controller.salvar_problema()
    @app.route('/problemas/atualizar')
    @login_required
    def atualizar_problema():
        return manutencao_controller.atualizar_status_problema()
    @app.route('/checklist')
    @login_required
    def form_checklist():
        return manutencao_controller.form_checklist()
    @app.route('/checklist/salvar', methods=['POST'])
    @login_required
    def salvar_checklist():
        return manutencao_controller.salvar_checklist()
    @app.route('/notificacoes')
    @login_required
    def listar_notificacoes():
        return notificacao_controller.listar_notificacoes()
    @app.route('/notificacoes/marcar_lida')
    @login_required
    def marcar_lida():
        return notificacao_controller.marcar_como_lida()
    @app.route('/notificacoes/deletar')
    @login_required
    def deletar_notificacao():
        return notificacao_controller.deletar_notificacao()
