# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 16/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface da área do estoquista (Menus da área do estoquista)---

# --- Import PyQt5
from PyQt5.QtWidgets import QWidget, QAction, QStackedWidget, QHBoxLayout
#import dos controllers
from controller.ControllerEstoquista import ControllerEstoquista
#Import das View
from view.TrocaSenha import TrocaSenha
from view.RelatorioSimples import RelatorioSimples
from view.CadastroProduto import CadastroProduto
from view.ListaProdutos import ListaProdutos
class AreaEstoquista(QWidget):
    '''Todos componentes graficos da área do gerente estão nesta classe'''
    def __init__(self, parent=None):
        super().__init__()
        self.main_class = parent#Variavel usada para acessar a classe principal
        self.controller = ControllerEstoquista(self)
        self.setCentralWidgets()
        self.setMenus()
        self.setLayoutEstoquista()
    def setMenus(self):
        '''Altera as opções do menubar para as necessidades do gerente'''
        self.main_class.main_menu.clear()
        #cria novas opções
        menu_cadastro = self.main_class.main_menu.addMenu("Cadastro")
        menu_relatorios = self.main_class.main_menu.addMenu("Relatórios")
        menu_produtos = self.main_class.main_menu.addMenu("Produtos")
        menu_sobre = self.main_class.main_menu.addMenu("Sobre")
        #---cria as ações do menu
        #-Menu de Cadastro
        act_troca_senha = QAction("Trocar Senha", self)
        act_desconectar = QAction("Desconectar", self)
        act_sair = QAction("Fechar",self)
        menu_cadastro.addAction(act_troca_senha)
        menu_cadastro.addAction(act_desconectar)
        menu_cadastro.addAction(act_sair)
        act_troca_senha.triggered.connect(self.controller.showTrocaSenha)
        act_desconectar.triggered.connect(self.controller.deconectar)
        act_sair.triggered.connect(self.main_class.close)
        #-Menu de Relatórios
        act_entra_saida = QAction("Relatório de Entrada e Saída", self)
        act_perdas = QAction("Relatório de Perdas", self)
        act_total_estoque = QAction("Relatório Total de Estoque", self)
        act_vencimentos_futuros = QAction("Relatório de Vencimentos Futuros", self)
        menu_relatorios.addAction(act_entra_saida)
        menu_relatorios.addAction(act_perdas)
        menu_relatorios.addAction(act_total_estoque)
        menu_relatorios.addAction(act_vencimentos_futuros)
        #-Menu Produtos
        act_cadastra_produto = QAction("Cadastrar Produtos", self)
        act_lista_produto = QAction("Listar Produtos", self)
        act_cadastra_unidade = QAction("Cadastrar Unidade", self)
        act_lista_unidade = QAction("Listar Unidade", self)
        act_cadastra_categoria = QAction("Cadastrar Categoria", self)
        act_lista_categoria = QAction("Listar Categoria", self)
        menu_produtos.addAction(act_cadastra_produto)
        menu_produtos.addAction(act_lista_produto)
        menu_produtos.addAction(act_cadastra_unidade)
        menu_produtos.addAction(act_lista_unidade)
        menu_produtos.addAction(act_cadastra_categoria)
        menu_produtos.addAction(act_lista_categoria)
        act_cadastra_produto.triggered.connect(self.controller.showCadastroProduto)
        act_lista_produto.triggered.connect(self.controller.showListaProdutos)
    def setCentralWidgets(self):
        '''Cria o Widget Central da tela da área do gerente'''
        #Cria os telas da área do cliente
        self.home_estoquista = RelatorioSimples(self)#Um relatorio simples é usado como tela inicial
        self.troca_senha = TrocaSenha(self)
        self.cadastro_produto = CadastroProduto(self)
        self.lista_produtos = ListaProdutos(self)
        #Cria o centralWidget da área do cliente
        self.conteudo_central = QStackedWidget(self)
        #Difine o primeiro widget do centralWidget
        self.conteudo_central.addWidget(self.home_estoquista)
        self.conteudo_central.setCurrentWidget(self.home_estoquista)
    def setLayoutEstoquista(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_conteudo = QHBoxLayout()
        self.layout_conteudo.addWidget(self.conteudo_central)
        self.setLayout(self.layout_conteudo)
        