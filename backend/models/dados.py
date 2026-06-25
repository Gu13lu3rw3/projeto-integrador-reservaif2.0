from database.conexao import conectar
from datetime import datetime


class Sala:
    def __init__(self, id, nome, capacidade, localizacao, status):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.status = status
        self.status_manutencao = status


class Reserva:
    def __init__(self, id, id_sala, id_professor, data, hora_inicio, hora_fim, motivo, status, justificativa_rejeicao, data_aprovacao_rejeicao, id_coordenador_aprovacao):
        self.id = id
        self.id_sala = id_sala
        self.id_professor = id_professor
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.motivo = motivo
        self.status = status
        self.justificativa_rejeicao = justificativa_rejeicao
        self.data_aprovacao_rejeicao = data_aprovacao_rejeicao
        self.aprovado_por = id_coordenador_aprovacao


class Usuario:
    def __init__(self, id, nome, email, senha, perfil):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil


class Problema:
    def __init__(self, id, id_sala, descricao, status, reportado_por, data_reporte, data_resolucao, resolvido_por):
        self.id = id
        self.id_sala = id_sala
        self.descricao = descricao
        self.status = status
        self.reportado_por = reportado_por
        self.data_reporte = data_reporte
        self.data_resolucao = data_resolucao
        self.resolvido_por = resolvido_por


class Notificacao:
    def __init__(self, id, id_usuario, mensagem, lida, data):
        self.id = id
        self.id_usuario = id_usuario
        self.mensagem = mensagem
        self.lida = lida
        self.data = data


def buscar_usuario_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USUARIO WHERE email = %s", (email,))
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()
    if linha:
        return Usuario(linha['id_usuario'], linha['nome'], linha['email'], linha['senha'], linha['perfil_acesso'])
    return None


def buscar_usuario_por_id(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USUARIO WHERE id_usuario = %s", (id_usuario,))
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()
    if linha:
        return Usuario(linha['id_usuario'], linha['nome'], linha['email'], linha['senha'], linha['perfil_acesso'])
    return None


def listar_todas_salas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM SALA")
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    salas = []
    for linha in linhas:
        salas.append(Sala(linha['id_sala'], linha['nome'], linha['capacidade'], linha['localizacao'], linha['status_manutencao']))
    return salas


def buscar_sala_por_id(id_sala):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM SALA WHERE id_sala = %s", (id_sala,))
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()
    if linha:
        return Sala(linha['id_sala'], linha['nome'], linha['capacidade'], linha['localizacao'], linha['status_manutencao'])
    return None


def inserir_sala(nome, capacidade, localizacao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO SALA (nome, capacidade, localizacao, status_manutencao) VALUES (%s, %s, %s, %s)",
        (nome, capacidade, localizacao, 'Disponível')
    )
    conexao.commit()
    cursor.close()
    conexao.close()


def atualizar_status_sala(id_sala, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE SALA SET status_manutencao = %s WHERE id_sala = %s", (novo_status, id_sala))
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_todas_reservas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM RESERVA ORDER BY data DESC, hora_inicio DESC")
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    reservas = []
    for linha in linhas:
        reservas.append(converter_linha_em_reserva(linha))
    return reservas


def buscar_reserva_por_id(id_reserva):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM RESERVA WHERE id_reserva = %s", (id_reserva,))
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()
    if linha:
        return converter_linha_em_reserva(linha)
    return None


def converter_linha_em_reserva(linha):
    return Reserva(
        linha['id_reserva'], linha['id_sala'], linha['id_professor'], str(linha['data']),
        str(linha['hora_inicio']), str(linha['hora_fim']), linha['motivo'], linha['status_reserva'],
        linha['justificativa_rejeicao'], linha['data_aprovacao_rejeicao'], linha['id_coordenador_aprovacao']
    )


def inserir_reserva(id_sala, id_professor, data, hora_inicio, duracao_minutos, hora_fim, motivo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO RESERVA (id_sala, id_professor, data, hora_inicio, duracao_minutos, hora_fim, motivo, status_reserva) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (id_sala, id_professor, data, hora_inicio, duracao_minutos, hora_fim, motivo, 'Pendente')
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conexao.close()
    return novo_id


def aprovar_reserva_no_banco(id_reserva, id_coordenador):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE RESERVA SET status_reserva = %s, id_coordenador_aprovacao = %s, data_aprovacao_rejeicao = NOW() WHERE id_reserva = %s",
        ('Aprovada', id_coordenador, id_reserva)
    )
    conexao.commit()
    cursor.close()
    conexao.close()


def rejeitar_reserva_no_banco(id_reserva, id_coordenador, justificativa):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE RESERVA SET status_reserva = %s, id_coordenador_aprovacao = %s, justificativa_rejeicao = %s, data_aprovacao_rejeicao = NOW() WHERE id_reserva = %s",
        ('Rejeitada', id_coordenador, justificativa, id_reserva)
    )
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_todos_problemas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PROBLEMA ORDER BY data_reporte DESC")
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    problemas = []
    for linha in linhas:
        problemas.append(converter_linha_em_problema(linha))
    return problemas


def buscar_problema_por_id(id_problema):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PROBLEMA WHERE id_problema = %s", (id_problema,))
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()
    if linha:
        return converter_linha_em_problema(linha)
    return None


def converter_linha_em_problema(linha):
    return Problema(
        linha['id_problema'], linha['id_sala'], linha['descricao'], linha['status_problema'],
        linha['id_professor_reporte'], str(linha['data_reporte']), linha['data_resolucao'],
        linha['id_manutencao_responsavel']
    )


def inserir_problema(id_sala, descricao, prioridade, id_professor_reporte):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO PROBLEMA (id_sala, id_professor_reporte, descricao, data_reporte, status_problema) VALUES (%s, %s, %s, NOW(), %s)",
        (id_sala, id_professor_reporte, descricao, 'Pendente')
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conexao.close()
    return novo_id


def atualizar_status_problema_no_banco(id_problema, novo_status, id_manutencao_responsavel):
    conexao = conectar()
    cursor = conexao.cursor()
    if novo_status == 'Resolvido':
        cursor.execute(
            "UPDATE PROBLEMA SET status_problema = %s, data_resolucao = NOW(), id_manutencao_responsavel = %s WHERE id_problema = %s",
            (novo_status, id_manutencao_responsavel, id_problema)
        )
    else:
        cursor.execute(
            "UPDATE PROBLEMA SET status_problema = %s WHERE id_problema = %s",
            (novo_status, id_problema)
        )
    conexao.commit()
    cursor.close()
    conexao.close()


def contar_problemas_pendentes_alta_prioridade(id_sala):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM PROBLEMA WHERE id_sala = %s AND status_problema != %s",
        (id_sala, 'Resolvido')
    )
    total = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return total


def listar_notificacoes_do_usuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM NOTIFICACAO WHERE id_usuario = %s ORDER BY data_hora DESC", (id_usuario,))
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    notificacoes = []
    for linha in linhas:
        notificacoes.append(Notificacao(linha['id_notificacao'], linha['id_usuario'], linha['mensagem'], linha['lida'], str(linha['data_hora'])))
    return notificacoes


def listar_todas_notificacoes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM NOTIFICACAO ORDER BY data_hora DESC")
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    notificacoes = []
    for linha in linhas:
        notificacoes.append(Notificacao(linha['id_notificacao'], linha['id_usuario'], linha['mensagem'], linha['lida'], str(linha['data_hora'])))
    return notificacoes


def deletar_notificacao_do_banco(id_notificacao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM NOTIFICACAO WHERE id_notificacao = %s", (id_notificacao,))
    conexao.commit()
    cursor.close()
    conexao.close()


def buscar_historico_reserva(id_reserva):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.*, s.nome as nome_sala, u.nome as nome_professor, c.nome as nome_coordenador
        FROM RESERVA r
        JOIN SALA s ON r.id_sala = s.id_sala
        JOIN USUARIO u ON r.id_professor = u.id_usuario
        LEFT JOIN USUARIO c ON r.id_coordenador_aprovacao = c.id_usuario
        WHERE r.id_reserva = %s
    """, (id_reserva,))
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()
    return linha


def calcular_tmr():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT data_reporte, data_resolucao FROM PROBLEMA WHERE status_problema = 'Resolvido'")
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    
    if not linhas:
        return 0
        
    total_horas = 0
    for linha in linhas:
        fmt = "%Y-%m-%d %H:%M:%S"
        try:
            inicio = linha['data_reporte'] if isinstance(linha['data_reporte'], datetime) else datetime.strptime(str(linha['data_reporte']), fmt)
            fim = linha['data_resolucao'] if isinstance(linha['data_resolucao'], datetime) else datetime.strptime(str(linha['data_resolucao']), fmt)
            diff = fim - inicio
            total_horas += diff.total_seconds() / 3600
        except:
            continue
            
    return round(total_horas / len(linhas), 1) if linhas else 0


def inserir_notificacao(id_usuario, tipo_notificacao, mensagem):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO NOTIFICACAO (id_usuario, tipo_notificacao, mensagem, data_hora, lida, meio_envio) VALUES (%s, %s, %s, NOW(), %s, %s)",
        (id_usuario, tipo_notificacao, mensagem, False, 'in-app')
    )
    conexao.commit()
    cursor.close()
    conexao.close()


def marcar_notificacao_como_lida(id_notificacao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE NOTIFICACAO SET lida = TRUE WHERE id_notificacao = %s", (id_notificacao,))
    conexao.commit()
    cursor.close()
    conexao.close()


def inserir_checklist(id_sala, id_manutencao_responsavel):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO CHECKLIST (id_sala, id_manutencao_responsavel, data_realizacao, status_checklist) VALUES (%s, %s, NOW(), %s)",
        (id_sala, id_manutencao_responsavel, 'Pendente')
    )
    conexao.commit()
    cursor.close()
    conexao.close()
