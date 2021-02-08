from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

# passando parâmetros para o sql via python, ideal pois evita ataques de SQL INJECTION
sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '98276-9898'),
    ('Flávia', '99276-3851'),
    ('Carlos', '99819-2812'),
    ('Pedro', '98571-1248'),
    ('Ana', '99276-9598'),
    ('Ana', '98776-9078'),
    ('Ana', '98118-1234')
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # indicando que o comando sql será executado várias vezes
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registros incluídos!')
