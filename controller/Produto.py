# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Produto---

# ---Import Pacotes do sistema
from model.Bd import Bd
from controller.CategoriaProduto import CategoriaProduto
class Produto(CategoriaProduto):
    def __init__(self, codigo_barras = None, lote = None, nome = None, unidade = None, quantidade = None,
                    peso = None, local_armazenamento = None, data_vencimento = None, ):
        super().__init__()
        self.id_produto = None
        #self.id_categoria = None
        self.codigo_barras = codigo_barras
        self.lote = lote
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.peso = peso
        self.local_armazenamento = local_armazenamento
        self.data_vencimento = data_vencimento
    def cadastraProduto(self):
        pass
    def alteraProduto(self):
        pass
    def deletaProduto(self):
        pass
    def getDadosProduto(self):
        '''Retorna uma Lista com os dados do Produto'''
        pass
    def getTotalProdutos(self):
        pass
    def getProdutosVencidos(self):
        pass