import controllers.controllers as controllers

# aqui eu defino todas as URLs do sistema
def adicionar_rotas(app):
    # rotas do jogo
    app.add_url_rule('/', 'index', controllers.index)
    app.add_url_rule('/jogo', 'jogo', controllers.jogo)
    app.add_url_rule('/responder', 'responder', controllers.responder, methods=['POST'])
    app.add_url_rule('/resetar', 'resetar', controllers.resetar)
    
    # rotas da parte de administração (crud)
    app.add_url_rule('/admin', 'admin_listar', controllers.admin_listar)
    app.add_url_rule('/admin/nova', 'admin_nova', controllers.admin_nova)
    app.add_url_rule('/admin/salvar', 'admin_salvar', controllers.admin_salvar, methods=['POST'])
    app.add_url_rule('/admin/editar/<int:id>', 'admin_editar', controllers.admin_editar)
    app.add_url_rule('/admin/excluir/<int:id>', 'admin_excluir', controllers.admin_excluir)
