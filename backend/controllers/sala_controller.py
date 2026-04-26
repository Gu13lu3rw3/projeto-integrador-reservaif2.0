from flask import jsonify
from models.sala import Sala

banco_salas = []

class SalaController:
    @staticmethod
    def cadastrar(dados):
        if not all(k in dados for k in ("nome", "capacidade", "localizacao")):
            return jsonify({"erro": "Dados da sala incompletos"}), 400
        
        nova_sala = Sala(dados['nome'], dados['capacidade'], dados['localizacao'])
        banco_salas.append(nova_sala.to_dict())
        
        return jsonify({
            "mensagem": "Sala cadastrada com sucesso!",
            "sala": nova_sala.to_dict()
        }), 201

    @staticmethod
    def listar():
        return jsonify(banco_salas), 200
