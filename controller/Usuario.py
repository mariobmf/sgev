# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Usuario---

# ---Import Pacotes do sistema
from model.Bd import Bd
from view.AreaGerente import AreaGerente
from view.AreaEstoquista import AreaEstoquista
from view.AreaAdmin import AreaAdmin

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
        bd = Bd()
        con = bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT id_tipo, numero_cracha, nome, sobrenome 
                        FROM usuario WHERE id_usuario=%s LIMIT 1""",(self.id_usuario,))
        result = cursor.fetchone()
        self.tipo_usuario = result[0]
        self.numero_cracha = result[1]
        self.nome = result[2]
        self.sobrenome = result[3]
    def autenticaUsuario(self):
        '''Retorna verdadeiro caso o usuário esteja cadastrado'''
        bd = Bd()
        con = bd.connectBd()
        cursor = con.cursor()
        values=(self.cpf,self.password)
        cursor.execute("SELECT id_usuario FROM usuario WHERE %s=cpf AND %s=passwd LIMIT 1",values)
        result = cursor.fetchone()
        con.close()
        if(result == None):
            return False   
        else:
            self.id_usuario = result[0]
            return True
    def getRota(self, parent):
        '''Retorna a rota que o usuário tem direito
        -Gerente - AreaGerente
        -Estoquista - AreaEstoquista
        -Administrador - AreaAdmin
        '''
        if self.tipo_usuario == 1:
            return AreaAdmin(parent)
        elif self.tipo_usuario == 2:
            return AreaGerente(parent)
        elif self.tipo_usuario == 3:
            return AreaEstoquista(parent)
        else:
            print("Rota não definida")