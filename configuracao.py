from mysql.connector import connect

conexao = connect(  # função com parâmetros nomeados
    host='localhost',
    port=3306,
    user='root',
    password='123456789'
)

print(conexao)
