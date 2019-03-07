# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções da área do estoquista---

from controller.Controller import Controller
from controller.Usuario import Usuario
from controller.Produto import Produto
from controller.Categoria import Categoria
from controller.Unidade import Unidade

class ControllerEstoquista(Controller):
    '''Todas funcções e ações da área do gerente estão nesta classe'''
    def __init__(self, parent):
        self.parent = parent# variavel usada para acessar a classe AreaGerente
        super().__init__(self.parent)
        self.produto = Produto(False)
        self.categoria = Categoria(False)
        self.unidade = Unidade(False)
    def showCadastroProduto(self):
        self.parent.conteudo_central.addWidget(self.parent.cadastro_produto)
        self.parent.conteudo_central.setCurrentWidget(self.parent.cadastro_produto)
    def showHome(self):
        self.parent.conteudo_central.setCurrentWidget(self.parent.home_estoquista)
    def cadastrarProduto(self):
        '''Cadastra um novo produto no sistema'''
        if(self.parent.cadastro_produto.verificaCamposVazios()):
            pass
        '''
        codigo = self.parent.cadastro_produto.edit_codigo.text()
        lote = self.parent.cadastro_produto.edit_lote.text()
        categoria = self.parent.cadastro_produto.cb_categoria.currentData()
        nome = self.parent.cadastro_produto.edit_nome.text()
        descricao = self.parent.cadastro_produto.edit_descricao.text()
        quantidade = self.parent.cadastro_produto.edit_quantidade.text()
        unidade = self.parent.cadastro_produto.cb_unidade.currentData()
        peso = self.parent.cadastro_produto.edit_peso.text()
        local = self.parent.cadastro_produto.edit_local.text()
        data = self.parent.cadastro_produto.edit_data.text()
        produto = Produto(None, categoria, unidade, codigo, lote, nome, descricao, quantidade, peso, local, data)
        if(produto.cadastraProduto()):
           self.parent.cadastro_produto.showMessageSucesso()'''