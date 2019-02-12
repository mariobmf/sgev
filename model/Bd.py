import mysql.connector
from mysql.connector import errorcode
class Bd():
    def __init__(self):
        self.config = {
            'user': 'devmario',
            'password': 'd3vm4r10',
            'host': 'localhost',
            'port': '3306',
            'database': 'sgev'
        }    
    def connectBd(self):
        '''Retorna uma conexao com o banco de dados'''
        try:
            con = mysql.connector.connect(**self.config)
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro com nome de usuário ou senha")
            elif erro.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de Dados não existe")
            else:
                print(erro)
        return(con)