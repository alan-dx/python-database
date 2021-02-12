from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'UPDATE contatos SET nome = %s WHERE id = %s'
args = ('Rafaela', 4)
# sql = 'SELECT * FROM contatos'


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
