import mysql.connector
import pyodbc

#print(pyodbc.drivers())

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='l88Gg#3s22',
    database='bdyoutube',
)
cursor = conexao.cursor()

# CRUD - READ
nome_produto = "refrigerante"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados



conexao.close()
cursor.close()

# CREATE

"""
nome_produto = "refrigerante"
valor = 8 # reais
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

"""

# READ

"""comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)
"""

# UPDATE

"""nome_produto = "refrigerante"
valor = 10
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados"""

# DELETE

"""nome_produto = "refrigerante"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados"""