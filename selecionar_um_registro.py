from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())  # fetchone retorna um único elemento por vez
