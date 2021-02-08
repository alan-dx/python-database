from bd import nova_conexao

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute('SHOW TABLES')

    # lembre-se que o cursor armazena todos os retornos dos comandos sql executados
    # enumerate numera os elementos dentro do objeto passado (cursor)
    for i, table in enumerate(cursor, start=1):
        print(f'Tabela {i}: {table[0]}')
