from controllers.sala_controller import listar_salas, form_cadastrar_sala, salvar_sala
from controllers.reserva_controller import listar_reservas, form_criar_reserva, salvar_reserva, aprovar_reserva, rejeitar_reserva, liberar_sala_automatica
from controllers.manutencao_controller import listar_problemas, form_reportar_problema, salvar_problema, form_checklist, salvar_checklist
from controllers.notificacao_controller import listar_notificacoes

def adicionar_rotas(app):
    # Rotas de Salas (HU08)
    app.add_url_rule('/salas', view_func=listar_salas)
    app.add_url_rule('/salas/novo', view_func=form_cadastrar_sala)
    app.add_url_rule('/salas/salvar', view_func=salvar_sala, methods=['POST'])

    # Rotas de Reservas (HU02, HU04, HU11)
    app.add_url_rule('/reservas', view_func=listar_reservas)
    app.add_url_rule('/reservas/novo', view_func=form_criar_reserva)
    app.add_url_rule('/reservas/salvar', view_func=salvar_reserva, methods=['POST'])
    app.add_url_rule('/reservas/aprovar', view_func=aprovar_reserva)
    app.add_url_rule('/reservas/rejeitar', view_func=rejeitar_reserva)
    app.add_url_rule('/reservas/liberar', view_func=liberar_sala_automatica)

    # Rotas de Manutenção (HU06, HU10)
    app.add_url_rule('/problemas', view_func=listar_problemas)
    app.add_url_rule('/problemas/novo', view_func=form_reportar_problema)
    app.add_url_rule('/problemas/salvar', view_func=salvar_problema, methods=['POST'])
    app.add_url_rule('/checklist', view_func=form_checklist)
    app.add_url_rule('/checklist/salvar', view_func=salvar_checklist, methods=['POST'])

    # Rotas de Notificações (HU09)
    app.add_url_rule('/notificacoes', view_func=listar_notificacoes)

    # Rota Inicial
    app.add_url_rule('/', view_func=listar_salas)
