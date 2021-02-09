from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # 2° parm são parametros de limitação passados para o comando sql
        cursor.execute(sql, (10, 0))
        # é indicado fazer uma paginação para limitar a busca, evitando problemas de desempenho
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            # :2d limita a dois digitos, 20s acrescenta 20 caracteres vazios
            print(f'{contato[2]:2d} - {contato[0]:20s} Telefone: {contato[1]}')
