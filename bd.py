from mysql.connector import connect
# módulo utilizado em conjunto com a declaração with
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678',
    database='agenda'
)


# gerencia o contexto da aplicação para ser passado para o bloco with, indicando o que deve ser feito no with
@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()  # libera o recurso
            print('finally...')
