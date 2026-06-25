import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root1234',
        database='reservaif'
    )
    return conexao
