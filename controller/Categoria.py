# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Categoria Produto---

# ---Import Pacotes do sistema
from model.Bd import Bd

class Categoria():
    def __init__(self, id_categoria = None, id_usuario = None, nome = None, descricao_categoria = None, tipo = None):
        print(id_categoria)
        self.id_categoria = id_categoria
        self.id_usuario = id_usuario
        self.nome = nome
        self.descricao_categoria = descricao_categoria
        self.tipo = tipo
        self.bd = Bd()
        if(id_categoria == None):
            print("Cadastrar")
            self.cadastraCategoria()
        else:
            self.setDadosCategoria()
    def cadastraCategoria(self):
        '''Cadastra uma nova categoria de produto no banco de dados'''
        try:
            con = self.bd.connectBd()
            cursor = con.cursor()
            values = (self.id_usuario, self.nome, self.descricao_categoria, self.tipo)
            cursor.execute("INSERT INTO categoria (id_usuario, nome, descricao, tipo) VALUES (%s,%s,%s,%s)",values)
            con.commit()
            return True
        except Exception as error:
            print("Erro: %s" % error)
        finally:
            if "con" in locals():
                con.close()
    def alteraCategoria(self):
        pass
    def deletaCategoria(self):
        pass
    def setDadosCategoria(self):
        '''Retorna uma Lista com os dados da Categoria e passa esses dados para a instancia do objeto'''
        con = self.bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT id_usuario, nome, descricao, tipo 
                        FROM categoria WHERE id_categoria=%s LIMIT 1""",(self.id_categoria,))
        result = cursor.fetchone()
        con.close()
        self.id_usuario = result[0]
        self.nome = result[1]
        self.descricao_categoria = result[2]
        self.tipo = result[3]
    def getTotalCategoria(self):
        pass