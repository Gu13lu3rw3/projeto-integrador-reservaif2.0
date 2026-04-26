from flask import jsonify
from models.problema import Problema

banco_problemas = []

class ProblemaController:
    @staticmethod
    def reportar(dados):
        if not all(k in dados for k in ("id_sala", "descricao", "id_professor_reporte")):
            return jsonify({"erro": "Dados do reporte incompletos"}), 400
        
        novo_problema = Problema(
            dados['id_sala'], 
            dados['descricao'], 
            dados['id_professor_reporte']
        )
        banco_problemas.append(novo_problema.to_dict())
        
        return jsonify({
            "mensagem": "Problema reportado com sucesso!",
            "problema": novo_problema.to_dict()
        }), 201
