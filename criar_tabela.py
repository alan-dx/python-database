from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50), 
        tel VARCHAR(40)
    )
"""

tabela_emails = """
    CREATE TABLE emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

# o bloco with é usado para garantir finalização de recursos adquiridos, garantindo que estes
# sejam fechados no momento certo, funciona como uma abreviação do try finally

try:
    with nova_conexao() as conexao:  # com o with a conexão é finalizada após a execução desse bloco
        # observe que a conexão só é encerrada (o bloco finally de nova_conexão()) após o bloco abaixo ser executado
        # isso ocorre por conta do decorator @contextmanager em conjunto com o with
        try:
            print('try')
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    # os erros que ocorrem fora do with acima, ou seja dentro arquivo bd.py deve ser tratos aqui
    print(f'Erro de CONEXÃO (bd.py file): {e.msg}')
