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

INSERT INTO USUARIO (nome, email, senha, perfil_acesso) VALUES 
('Guilherme Silva', 'guilherme@ifpi.edu.br', '$2b$12$eImiTXuWVxjM72fGC3W/m.', 'Admin'),
('Carlos Eduardo', 'carlos@ifpi.edu.br', '$2b$12$eImiTXuWVxjM72fGC3W/m.', 'Coordenador'),
('Antônio Marcos', 'antonio@ifpi.edu.br', '$2b$12$eImiTXuWVxjM72fGC3W/m.', 'Professor'),
('Equipe Manutenção', 'manutencao@ifpi.edu.br', '$2b$12$eImiTXuWVxjM72fGC3W/m.', 'Manutenção');

INSERT INTO SALA (nome, capacidade, localizacao, status_manutencao) VALUES 
('Sala B2-01', 40, 'Bloco B - Piso 2', 'Disponível'),
('Laboratório TDS', 30, 'Bloco A - Piso 1', 'Disponível'),
('Auditório Central', 150, 'Bloco C', 'Disponível');

INSERT INTO EQUIPAMENTO (nome, descricao, id_sala) VALUES 
('Projetor Epson', 'Modelo X41+', 1),
('Ar Condicionado', 'Split 18000 BTUs', 1),
('Projetor BenQ', 'Modelo MW535', 2);

INSERT INTO HORARIO_OFICIAL (id_sala, dia_semana, hora_inicio, hora_fim, descricao) VALUES 
(1, 'Segunda-feira', '07:30:00', '09:10:00', 'Engenharia de Software (TDS)'),
(1, 'Segunda-feira', '09:20:00', '11:00:00', 'Programação back-end (TDS)'),
(2, 'Segunda-feira', '13:30:00', '15:10:00', 'Programação Orientada a Objetos (TDS)');
