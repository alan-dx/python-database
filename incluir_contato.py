from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

# passando parâmetros para o sql via python, ideal pois evita ataques de SQL INJECTION
sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Lucas', '98152-1231')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()  # necessário para que as alterações sejam salvas no banco de dados
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('1 registo incluído, ID: ', cursor.lastrowid)
