# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Categoria Produto---

# ---Import Pacotes do sistema
from model.Bd import Bd

class CategoriaProduto():
    def __init__(self):
        self.id_categoria = None
        self.id_usuario = None
        self.nome = None
        self.descricao = None
        self.tipo = None
    def cadastraCategoria(self):
        pass
    def alteraCategoria(self):
        pass
    def deletaCategoria(self):
        pass
    def getDadosCategoria(self):
        '''Retorna uma Lista com os dados da Categoria'''
        pass
    def getTotalCategoria(self):
        pass