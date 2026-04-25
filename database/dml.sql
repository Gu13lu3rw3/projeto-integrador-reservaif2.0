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
