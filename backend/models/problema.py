from datetime import datetime

class Problema:
    def __init__(self, id_sala, descricao, id_professor_reporte):
        self.id_sala = id_sala
        self.descricao = descricao
        self.id_professor_reporte = id_professor_reporte
        self.data_reporte = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = "Pendente"

    def to_dict(self):
        return {
            "id_sala": self.id_sala,
            "descricao": self.descricao,
            "id_professor_reporte": self.id_professor_reporte,
            "data_reporte": self.data_reporte,
            "status": self.status
        }
