from mysql.connector import connect

conexao = connect(  # função com parâmetros nomeados
    host='localhost',
    port=3306,
    user='root',
    password='12345678'
)

cursor = conexao.cursor()  # executa os comandos sql e armazena os resultados
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')
