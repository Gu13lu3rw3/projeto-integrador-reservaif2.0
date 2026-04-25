CREATE TABLE USUARIO (
id_usuario INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
senha VARCHAR(255) NOT NULL,
perfil_acesso VARCHAR(50) NOT NULL
);

CREATE TABLE SALA (
id_sala INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL UNIQUE,
capacidade INT NOT NULL,
localizacao VARCHAR(255) NOT NULL,
status_manutencao VARCHAR(50) NOT NULL DEFAULT
);

CREATE TABLE EQUIPAMENTO (
id_equipamento INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
descricao TEXT,
id_sala INT NOT NULL,
FOREIGN KEY (id_sala) REFERENCES SALA(id_sala));
);

CREATE TABLE RESERVA (
id_reserva INT PRIMARY KEY AUTO_INCREMENT,
id_sala INT NOT NULL,
id_professor INT NOT NULL,
data DATE NOT NULL,
hora_inicio TIME NOT NULL,
duracao_minutos INT NOT NULL,
hora_fim TIME NOT NULL,
motivo TEXT NOT NULL,
status_reserva VARCHAR(50) NOT NULL DEFAULT
justificativa_rejeicao TEXT,
data_aprovacao_rejeicao DATETIME,
id_coordenador_aprovacao INT,
FOREIGN KEY (id_sala) REFERENCES SALA(id_sala),
FOREIGN KEY (id_professor) REFERENCES USUARIO(id_usuario),
FOREIGN KEY (id_coordenador_aprovacao) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE HORARIO_OFICIAL (
id_horario_oficial INT PRIMARY KEY AUTO_INCREMENT,
id_sala INT NOT NULL,
dia_semana VARCHAR(20) NOT NULL,
hora_inicio TIME NOT NULL,
hora_fim TIME NOT NULL,
descricao VARCHAR(255),
FOREIGN KEY (id_sala) REFERENCES SALA(id_sala)
);

CREATE TABLE PROBLEMA (
id_problema INT PRIMARY KEY AUTO_INCREMENT,
id_sala INT NOT NULL,
id_equipamento INT
,id_professor_reporte INT NOT NULL,
descricao TEXT NOT NULL,
data_reporte DATETIME NOT NULL,
status_problema VARCHAR(50) NOT NULL DEFAULT
historico_status JSON,
data_resolucao DATETIME,
id_manutencao_responsavel INT,
FOREIGN KEY (id_sala) REFERENCES SALA(id_sala),
FOREIGN KEY (id_equipamento) REFERENCES EQUIPAMENTO(id_equipamento),
FOREIGN KEY (id_professor_reporte) REFERENCES USUARIO(id_usuario),
FOREIGN KEY (id_manutencao_responsavel) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE NOTIFICACAO (
id_notificacao INT PRIMARY KEY AUTO_INCREMENT,
id_usuario INT NOT NULL,
tipo_notificacao VARCHAR(100) NOT NULL,
mensagem TEXT NOT NULL,
data_hora DATETIME NOT NULL,
lida BOOLEAN NOT NULL DEFAULT FALSE,
meio_envio VARCHAR(50) NOT NULL,
id_referencia INT,
FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE CHECKLIST (
id_checklist INT PRIMARY KEY AUTO_INCREMENT,
id_sala INT NOT NULL,
id_manutencao_responsavel INT NOT NULL,
data_realizacao DATETIME NOT NULL,
status_checklist VARCHAR(50) NOT NULL DEFAULT 'Pendente', 
itens_verificados JSON,
taxa_falha DECIMAL(5,2),
FOREIGN KEY (id_sala) REFERENCES SALA(id_sala),
FOREIGN KEY (id_manutencao_responsavel) REFERENCES USUARIO(id_usuario)
);
