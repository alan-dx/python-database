from bd import nova_conexao

# realizando uma busca onde a coluna nome dos elementos deve ter a letra indicada '%letra%'
sql = "SELECT * FROM contatos WHERE nome LIKE '%ia'"

# '%' => indica que pode conter algo antes ou depos
# '%a%'=> contém a letra a em alguma parte da palavra
# 'a%' => começa com a letra a
# '%a' => acaba com a letra a

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
