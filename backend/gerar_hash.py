import bcrypt

senha = 'senha123'
hash_gerado = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
print(hash_gerado.decode('utf-8'))
