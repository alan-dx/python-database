# --- LISTANDO OS BANCOS DE DADOS ---
from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    password='12345678'
)

cursor = conexao.cursor()  # executa os comandos sql e armazena os resultados
cursor.execute('SHOW DATABASES')

# enumerate é uma função que retorna um objeto iterável (no caso uma tupla), gerando uma numeração pra cada elemento do objeto passado
for i, database in enumerate(cursor):
    # cada posição da tupla retornada representa uma coluna da query realizada
    print(f'Banco de Dados {i}: {database[0]}')
