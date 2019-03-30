# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 23/02/2019 - Alterado
# VERSÂO 2.0
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções da área do estoquista---

from controller.Controller import Controller
from controller.Usuario import Usuario
from controller.Produto import Produto
from controller.Categoria import Categoria
from controller.Unidade import Unidade
# ----Import View
from view.CadastroProduto import CadastroProduto
from view.ListaProdutos import ListaProdutos
from view.EditProduto import EditProduto

class ControllerEstoquista(Controller):
    '''Todas funcções e ações da área do gerente estão nesta classe'''
    def __init__(self, parent):
        self.parent = parent# variavel usada para acessar a classe AreaGerente
        super().__init__(self.parent)
        self.produto = Produto(False)
        self.categoria = Categoria(False)
        self.unidade = Unidade(False)
    def showCadastroProduto(self):
        '''Exibe a subwindow de cadastro de produto'''
        self.sub_cadastro_produto = CadastroProduto(self)
        self.parent.mdi_area.addSubWindow(self.sub_cadastro_produto)
        self.sub_cadastro_produto.show()
    def showHome(self):
        self.parent.conteudo_central.setCurrentWidget(self.parent.home_estoquista)
    def showListaProdutos(self):
        '''Exibe a subwindow de lista de produto'''
        self.sub_lista_produto = ListaProdutos(self)
        self.parent.mdi_area.addSubWindow(self.sub_lista_produto)
        self.sub_lista_produto.show()
    def cadastrarProduto(self):
        '''Cadastra um novo produto no sistema'''
        if(self.sub_cadastro_produto.verificaCamposVazios()):
            codigo = self.sub_cadastro_produto.edit_codigo.text()
            lote = self.sub_cadastro_produto.edit_lote.text()
            categoria = self.sub_cadastro_produto.cb_categoria.currentData()
            nome = self.sub_cadastro_produto.edit_nome.text()
            descricao = self.sub_cadastro_produto.edit_descricao.text()
            quantidade = self.sub_cadastro_produto.edit_quantidade.text()
            unidade = self.sub_cadastro_produto.cb_unidade.currentData()
            peso = self.sub_cadastro_produto.edit_peso.text()
            local = self.sub_cadastro_produto.edit_local.text()
            data = self.sub_cadastro_produto.edit_data.text()
            produto = Produto(None, categoria, unidade, codigo, lote, nome, descricao, quantidade, peso, local, data)
            if(produto.cadastraProduto()):
                if(self.sub_cadastro_produto.showMessageSucesso() == False):
                    self.parent.mdi_area.removeSubWindow(self.sub_cadastro_produto)#remove a subwindow da tela
                    del self.sub_cadastro_produto#deleta a instancia da subwindow
    def editProduto(self,id_produto):
        pass
    def viewProduto(self,id_produto):
        pass
    def deleteProduto(self,id_produto):
        produto_del = Produto(id_produto)
        if(produto_del.deletaProduto() == True):
            del produto_del
            return True   