
from datetime import datetime
class Sala:
    def __init__(self, id, nome, capacidade, localizacao, recursos, status="Disponível"):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.recursos = recursos
        self.status = status
class Reserva:
    def __init__(self, id, id_sala, id_professor, data, hora_inicio, hora_fim, motivo, status="Pendente"):
        self.id = id
        self.id_sala = id_sala
        self.id_professor = id_professor
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.motivo = motivo
        self.status = status
        self.aprovado_por = None
        self.justificativa_rejeicao = None
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.data_atualizacao = self.data_criacao
        self.historico = [{"evento": "Reserva solicitada", "data_hora": self.data_criacao}]
class Usuario:
    def __init__(self, id, nome, email, senha, perfil):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
class Problema:
    def __init__(self, id, id_sala, descricao, prioridade, status="Pendente", reportado_por=None):
        self.id = id
        self.id_sala = id_sala
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.reportado_por = reportado_por
        self.data_reporte = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.data_resolucao = None
        self.resolvido_por = None
class Notificacao:
    def __init__(self, id, id_usuario, mensagem, lida=False):
        self.id = id
        self.id_usuario = id_usuario
        self.mensagem = mensagem
        self.lida = lida
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M")
salas = [
    Sala(1, "Laboratório de Informática 1", 30, "Bloco A - Piso 1", ["30 computadores", "Projetor", "Ar-condicionado"]),
    Sala(2, "Auditório Central", 150, "Bloco C - Térreo", ["Sistema de som", "Projetor", "Palco"]),
    Sala(3, "Sala de Aula 102", 40, "Bloco B - Piso 2", ["Quadro branco", "Ar-condicionado"])
]
usuarios = [
    Usuario(1, "João Professor", "joao@email.com", "123456", "Professor"),
    Usuario(2, "Maria Coordenadora", "maria@email.com", "123456", "Coordenador"),
    Usuario(3, "Silva Administrador", "silva@email.com", "123456", "Administrador"),
    Usuario(4, "Carlos Manutenção", "carlos@email.com", "123456", "Manutenção")
]
reservas = []
problemas = []
notificacoes = []
checklists = []
