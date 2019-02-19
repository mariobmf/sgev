# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções comuns para todas Contas---

from model.Bd import Bd

class Conta():
    def __init__(self, id_conta):
        self.id_conta = id_conta
        self.descricao = None
        if(self.id_conta != None):
            self.getDadosConta()
    def getDadosConta(self):
        '''Retorna uma Lista com os dados da Conta'''
        bd = Bd()
        con = bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT descricao 
                        FROM conta WHERE id_conta=%s LIMIT 1""",(self.id_conta,))
        result = cursor.fetchone()
        self.descricao = result[0]