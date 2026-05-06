class Questao:
    # aqui eu defini como cada questão vai ser estruturada
    def __init__(self, id, pergunta, a, b, c, resposta):
        self.id = id
        self.pergunta = pergunta
        self.a = a
        self.b = b
        self.c = c
        self.resposta = resposta
    
    # esse método serve para converter o objeto em um dicionário (ajuda na hora de mandar pro html)
    def to_dict(self):
        return {
            'id': self.id,
            'pergunta': self.pergunta,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'resposta': self.resposta
        }
