# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Unidade Produto---

# ---Import Pacotes do sistema
from model.Bd import Bd

class Unidade():
    def __init__(self, id_unidade=None, sigla=None, descricao_unidade=None):
        '''Construtor da Classe, Iniciar o construtor das seguintes maneiras:
        -Unidade(id_unidade=int) = Quando for preciso consultar ou modificar uma unidade especifica
        -Unidade(sigla, descricao_unidade) = Quando for cadastrar uma unidade
        -Unidade(id_unidade=False) = Quando for fazer uma consulta em todos categoria '''
        self.id_unidade = id_unidade
        self.sigla = sigla
        self.descricao_unidade = descricao_unidade
        self.bd = Bd()
        if(self.id_unidade == None):
            self.cadastraUnidade()
        elif(self.id_unidade != False):
            self.setDadosUnidade()
    def cadastraUnidade(self):
        '''Cadastra uma nova Unidade de produto no banco de dados'''
        try:
            con = self.bd.connectBd()
            cursor = con.cursor()
            values = (self.sigla, self.descricao_unidade)
            cursor.execute("INSERT INTO unidade (sigla, descricao) VALUES (%s,%s)",values)
            con.commit()
            return True
        except Exception as error:
            print("Erro: %s" % error)
        finally:
            if "con" in locals():
                con.close()
    def alteraUnidade(self):
        pass
    def deletaUnidade(self):
        pass
    def setDadosUnidade(self):
        '''Retorna uma Lista com os dados da Unidade e passa esses dados para a instancia do objeto'''
        try:
            con = self.bd.connectBd()
            cursor = con.cursor()
            cursor.execute("""SELECT sigla, descricao 
                            FROM unidade WHERE id_unidade=%s LIMIT 1""",(self.id_unidade,))
            result = cursor.fetchone()
            #con.close()
            self.sigla = result[0]
            self.descricao_unidade = result[1]
        except Exception as error:
            print(error)
        finally:
            if "con" in locals():
                con.close()
    def getUnidades(self):
        '''Retorna uma Lista com os nomes das Unidades'''
        try:
            con = self.bd.connectBd()
            cursor = con.cursor()
            cursor.execute("""SELECT id_unidade,sigla,descricao FROM unidade ORDER BY descricao ASC""")
            result = cursor.fetchall()
            #con.close()
            return result
        except Exception as error:
            print(error)
        finally:
            if "con" in locals():
                con.close()