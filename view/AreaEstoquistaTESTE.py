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
        