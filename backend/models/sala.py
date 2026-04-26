class Sala:
    def __init__(self, nome, capacidade, localizacao):
        self.nome = nome
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.status_manutencao = "Disponível"

    def to_dict(self):
        return {
            "nome": self.nome,
            "capacidade": self.capacidade,
            "localizacao": self.localizacao,
            "status_manutencao": self.status_manutencao
        }
