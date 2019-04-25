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
from view.CadastroUnidade import CadastroUnidade
from view.ListaProdutos import ListaProdutos
from view.ListaUnidades import ListaUnidades
from view.EditProduto import EditProduto
from view.ViewProduto import ViewProduto

class ControllerEstoquista(Controller):
    '''Todas funcções e ações da área do gerente estão nesta classe'''
    def __init__(self, parent):
        self.parent = parent# variavel usada para acessar a classe AreaGerente
        super().__init__(self.parent)
        self.produto = Produto(False)
        self.categoria = Categoria(False)
        self.unidade = Unidade(False)
    def showHome(self):
        self.parent.conteudo_central.setCurrentWidget(self.parent.home_estoquista)
    def showCadastroProduto(self):
        '''Exibe a subwindow de cadastro de produto'''
        self.sub_cadastro_produto = CadastroProduto(self)
        self.parent.mdi_area.addSubWindow(self.sub_cadastro_produto)
        self.sub_cadastro_produto.show()
    def showListaProdutos(self):
        '''Exibe a subwindow de lista de produto'''
        self.sub_lista_produto = ListaProdutos(self)
        self.parent.mdi_area.addSubWindow(self.sub_lista_produto)
        self.sub_lista_produto.show()
    def showCadastroUnidade(self):
        '''Exibe a subwindow de cadastro de unidade'''
        self.sub_cadastro_unidade = CadastroUnidade(self)
        self.parent.mdi_area.addSubWindow(self.sub_cadastro_unidade)
        self.sub_cadastro_unidade.show()
    def showListaUnidades(self):
        '''Exibe a subwindow de lista de unidades'''
        self.sub_lista_unidade = ListaUnidades(self)
        self.parent.mdi_area.addSubWindow(self.sub_lista_unidade)
        self.sub_lista_unidade.show()        
    def cadastrarProduto(self):
        '''Cadastra um novo produto no sistema'''
        if(self.sub_cadastro_produto.base_form.verificaCamposVazios()):
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
                    try:
                        self.sub_lista_produto.updateTable()
                    except:
                        pass
    def editarProduto(self):
        '''Edita os dados do produto'''
        if(self.sub_edit_produto.verificaCamposVazios()):
            codigo = self.sub_edit_produto.edit_codigo.text()
            lote = self.sub_edit_produto.edit_lote.text()
            categoria = self.sub_edit_produto.cb_categoria.currentData()
            nome = self.sub_edit_produto.edit_nome.text()
            descricao = self.sub_edit_produto.edit_descricao.text()
            quantidade = self.sub_edit_produto.edit_quantidade.text()
            unidade = self.sub_edit_produto.cb_unidade.currentData()
            peso = self.sub_edit_produto.edit_peso.text()
            local = self.sub_edit_produto.edit_local.text()
            data = self.sub_edit_produto.edit_data.text()
            produto = Produto(self.sub_edit_produto.produto[0]) 
            if(produto.alteraProduto(categoria, unidade, codigo, lote, nome, descricao, quantidade, peso, local, data)):
                self.sub_edit_produto.showMessageSucesso()#Mostra um dialogo se sucesso
                self.parent.mdi_area.removeSubWindow(self.sub_edit_produto)#remove a subwindow da tela
                del self.sub_edit_produto#deleta a instancia da subwindow
                self.sub_lista_produto.updateTable()#Chama a função para atualizar os dados da tabela
    def editProduto(self,id_produto):
        '''Pega os dados do produto e chama a tela de edição'''
        produto = Produto(id_produto)
        info_produto = [produto.id_produto, 
                        produto.codigo_barras, 
                        produto.lote,
                        produto.categoria.nome,
                        produto.nome,
                        produto.descricao_produto,
                        produto.quantidade,
                        produto.unidade.sigla,
                        produto.peso,
                        produto.local_armazenamento,
                        produto.data_vencimento]
        self.sub_edit_produto = EditProduto(self,info_produto)
        self.parent.mdi_area.addSubWindow(self.sub_edit_produto)
        self.sub_edit_produto.show()
    def viewProduto(self,id_produto):
        '''Exibe as informações do produto em uma janela de formulario'''
        produto = Produto(id_produto)
        info_produto = [produto.id_produto, 
                        produto.codigo_barras, 
                        produto.lote,
                        produto.categoria.nome,
                        produto.nome,
                        produto.descricao_produto,
                        produto.quantidade,
                        produto.unidade.sigla,
                        produto.peso,
                        produto.local_armazenamento,
                        produto.data_vencimento]
        self.sub_view_produto = ViewProduto(self,info_produto)
        self.parent.mdi_area.addSubWindow(self.sub_view_produto)
        self.sub_view_produto.show()
    def deleteProduto(self,id_produto):
        '''Deleta o produto'''
        produto_del = Produto(id_produto)
        if(produto_del.deletaProduto() == True):
            del produto_del
            self.sub_lista_produto.updateTable()   