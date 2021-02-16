from bd import nova_conexao
from mysql.connector import ProgrammingError

povar_grupo = 'INSERT INTO grupos(descricao) VALUES (%s)'

args = (
    ('Casa',),
    ('Trabalho',),
    ('Amigos',)
)

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(povar_grupo, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'Foram incluídos {cursor.rowcount} registros!')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
