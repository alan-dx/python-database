from bd import nova_conexao

# o bloco with é usado para garantir finalização de recursos adquiridos, garantindo que estes
# serão fechados no momento certo, funciona como uma abreviação do try finally
with nova_conexao() as conexao:
    if conexao.is_connected():
        print('Conectado!')

print('Fim:')
