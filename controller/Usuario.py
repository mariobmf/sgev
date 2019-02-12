# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Usuario---

# ---Import Pacotes do sistema
from model.Bd import Bd

class Usuario():
    def __init__(self, cpf = None, password=None, numero_cracha = None, nome = None, sobrenome = None, tipo_usuario = None):
        self.id_usuario = None
        self.cpf = cpf
        self.password = password
        self.numero_cracha = numero_cracha
        self.nome = nome
        self.sobrenome = sobrenome
        self.tipo_usuario = tipo_usuario
    def criaUsuario(self):
        pass
    def alteraUsuario(self):
        pass
    def deletaUsuario(self):
        pass
    def getDadosUsuario(self):
        '''Retorna uma Lista com os dados do Usuário'''
        pass
    def autenticaUsuario(self):
        '''Retorna verdadeiro caso o usuário esteja cadastrado'''
        bd = Bd()
        con = bd.connectBd()
        cursor = con.cursor()
        values=(self.cpf,self.password)
        cursor.execute("SELECT * FROM usuario WHERE %s=cpf AND %s=passwd",values)
        result = cursor.fetchone()
        con.close()
        if(result == None):
            return False   
        else:
            return True