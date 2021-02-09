from bd import nova_conexao

sql = 'SELECT * FROM contatos WHERE nome LIKE %s'

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%', )  # criar uma tupla com os argumentos

    cursor = conexao.cursor()
    cursor.execute(sql, args)  # evita sql injection

    for x in cursor:
        print(x)
