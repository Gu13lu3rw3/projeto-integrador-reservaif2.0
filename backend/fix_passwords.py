import bcrypt

senha = '123456'
hash_gerado = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

print(f"Hash para '123456': {hash_gerado}")

usuarios = [
    ('Guilherme Silva', 'guilherme@ifpi.edu.br', 'Admin'),
    ('Carlos Eduardo', 'carlos@ifpi.edu.br', 'Coordenador'),
    ('Antônio Marcos', 'antonio@ifpi.edu.br', 'Professor'),
    ('Equipe Manutenção', 'manutencao@ifpi.edu.br', 'Manutenção')
]

for nome, email, perfil in usuarios:
    print(f"INSERT INTO USUARIO (nome, email, senha, perfil_acesso) VALUES ('{nome}', '{email}', '{hash_gerado}', '{perfil}');")
