import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='l88Gg#3s22',
    database='bdyoutube',
)
cursor = conexao.cursor()

# CRUD - CREATE

nome_produto = "todynho"
valor = 3 # reais
comando = 'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


# resultado = cursor.fetchall() # ler o banco de dados




cursor.close()









conexao.close()
cursor.close()