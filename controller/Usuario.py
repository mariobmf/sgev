# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Usuario---

# ---Import Pacotes do sistema
from controller.Conta import Conta
from model.Bd import Bd

class Usuario(Conta):
    def __init__(self, cpf = None, password=None, numero_cracha = None, nome = None, sobrenome = None, id_conta = None):
        self.id_usuario = None
        self.cpf = cpf
        self.password = password
        self.numero_cracha = numero_cracha
        self.nome = nome
        self.sobrenome = sobrenome
        self.bd = Bd()
        if(id_conta != None):
            super().__init__(id_conta)
    def cadastraUsuario(self):
        '''Cadastra um novo usuário no banco de dados'''
        try:
            con = self.bd.connectBd()
            cursor = con.cursor()
            values = (self.id_conta, self.cpf, self.numero_cracha, self.nome, self.sobrenome, self.password)
            cursor.execute("INSERT INTO usuario (id_conta,cpf,numero_cracha,nome,sobrenome,passwd) VALUES (%s,%s,%s,%s,%s,%s)",values)
            con.commit()
            return True
        except Exception as error:
            print("Erro: %s" % error)
        finally:
            if "con" in locals():
                con.close()
    def alteraUsuario(self):
        pass
    def deletaUsuario(self):
        pass
    def alteraSenha(self):
        '''Altera a senha do usuário no banco de dados'''
        try:
            con = self.bd.connectBd()    
            cursor = con.cursor()
            cursor.execute("UPDATE usuario SET passwd = %s WHERE id_usuario=%s",(self.password,self.id_usuario))
            con.commit()
            return True
        except Exception as error:
            print(error)
        finally:
            if "con" in locals():
                con.close()
    def setDadosUsuario(self):
        '''Retorna uma Lista com os dados do Usuário'''
        con = self.bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT id_conta, numero_cracha, nome, sobrenome 
                        FROM usuario WHERE id_usuario=%s LIMIT 1""",(self.id_usuario,))
        result = cursor.fetchone()
        self.numero_cracha = result[1]
        self.nome = result[2]
        self.sobrenome = result[3]
        super().__init__(result[0])#Inicia a conta com o id_conta
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
            self.setDadosUsuario()
            return True
        