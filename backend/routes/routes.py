from flask import redirect, url_for
from controllers import (
    sala_controller, reserva_controller, auth_controller,
    notificacao_controller, manutencao_controller, disponibilidade_controller,
    dashboard_controller, api_controller
)


def index():
    return redirect(url_for('login'))


def adicionar_rotas(app):
    app.add_url_rule('/', 'index', index)

    app.add_url_rule('/login', 'login', auth_controller.form_login)
    app.add_url_rule('/login/bypass', 'login_bypass', auth_controller.login_bypass)
    app.add_url_rule('/processar_login', 'processar_login', auth_controller.processar_login, methods=['POST'])
    app.add_url_rule('/logout', 'logout', auth_controller.logout)
    app.add_url_rule('/recuperar_senha', 'recuperar_senha', auth_controller.form_recuperar_senha)
    app.add_url_rule('/recuperar_senha/processar', 'processar_recuperacao', auth_controller.processar_recuperacao_senha, methods=['POST'])
    app.add_url_rule('/recuperar_senha/confirmar', 'confirmar_recuperacao', auth_controller.confirmar_recuperacao)
    app.add_url_rule('/dashboard', 'dashboard', auth_controller.dashboard)

    app.add_url_rule('/dashboard/indicadores', 'dashboard_indicadores', dashboard_controller.exibir_indicadores)
    app.add_url_rule('/relatorios', 'relatorios', dashboard_controller.relatorios)
    app.add_url_rule('/relatorios/exportar', 'exportar_relatorio', dashboard_controller.exportar_relatorio_csv)

    app.add_url_rule('/salas', 'listar_salas', sala_controller.listar_salas)
    app.add_url_rule('/salas/novo', 'form_sala', sala_controller.form_sala)
    app.add_url_rule('/salas/salvar', 'salvar_sala', sala_controller.salvar_sala, methods=['POST'])

    app.add_url_rule('/reservas', 'listar_reservas', reserva_controller.listar_reservas)
    app.add_url_rule('/reservas/novo', 'form_reserva', reserva_controller.form_reserva)
    app.add_url_rule('/reservas/salvar', 'salvar_reserva', reserva_controller.salvar_reserva, methods=['POST'])
    app.add_url_rule('/reservas/aprovar', 'aprovar_reserva', reserva_controller.aprovar_reserva)
    app.add_url_rule('/reservas/rejeitar/form', 'form_rejeitar', reserva_controller.form_rejeitar)
    app.add_url_rule('/reservas/rejeitar/processar', 'processar_rejeicao', reserva_controller.processar_rejeicao, methods=['POST'])
    app.add_url_rule('/reservas/detalhe', 'detalhe_reserva', reserva_controller.detalhe_reserva)
    app.add_url_rule('/reservas/liberar', 'liberar_reservas', reserva_controller.liberar_reservas_automatico)

    app.add_url_rule('/disponibilidade', 'consultar_disponibilidade', disponibilidade_controller.form_consulta)
    app.add_url_rule('/disponibilidade/filtrar', 'filtrar_disponibilidade', disponibilidade_controller.filtrar, methods=['POST'])

    app.add_url_rule('/problemas', 'listar_problemas', manutencao_controller.listar_problemas)
    app.add_url_rule('/problemas/novo', 'form_problema', manutencao_controller.form_problema)
    app.add_url_rule('/problemas/salvar', 'salvar_problema', manutencao_controller.salvar_problema, methods=['POST'])
    app.add_url_rule('/problemas/atualizar', 'atualizar_problema', manutencao_controller.atualizar_status_problema)
    app.add_url_rule('/checklist', 'form_checklist', manutencao_controller.form_checklist)
    app.add_url_rule('/checklist/salvar', 'salvar_checklist', manutencao_controller.salvar_checklist, methods=['POST'])

    app.add_url_rule('/notificacoes', 'listar_notificacoes', notificacao_controller.listar_notificacoes)
    app.add_url_rule('/notificacoes/marcar_lida', 'marcar_lida', notificacao_controller.marcar_como_lida)
    app.add_url_rule('/notificacoes/deletar', 'deletar_notificacao', notificacao_controller.deletar_notificacao)
    
    app.add_url_rule('/api/salas', 'api_get_salas', api_controller.get_salas)
    app.add_url_rule('/api/stats', 'api_get_stats', api_controller.get_estatisticas)
