try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySql Connector não instalado!')
else:
    print('MySql Connector instalado e pronto!')
finally:
    print('\n Fim!')
