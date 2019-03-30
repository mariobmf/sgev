# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface da área do genrete (Menus da área do gerente)---

# --- Import PyQt5
from PyQt5.QtWidgets import QMdiSubWindow, QAction, QMdiArea, QHBoxLayout
#import dos controllers
from controller.ControllerGerente import ControllerGerente
#Import das View
from view.TrocaSenha import TrocaSenha
from view.CadastroEstoquista import CadastroEstoquista
from view.RelatorioSimples import RelatorioSimples
class AreaGerente(QMdiSubWindow):
    '''Todos componentes graficos da área do gerente estão nesta classe'''
    def __init__(self, parent=None):
        super().__init__()
        self.main_class = parent#Variavel usada para acessar a classe principal
        self.controller = ControllerGerente(self)
        self.setCentralWidgets()
        self.setMenus()
        self.setLayoutGerente()
    def setCentralWidgets(self):
        '''Cria o Widget Central da tela da área do gerente'''
        #Cria os telas da área do cliente
        self.home_gerente = RelatorioSimples(self)#Um relatorio simples é usado como tela inicial
        self.cadastro_estoquista = CadastroEstoquista(self)
        self.troca_senha = TrocaSenha(self)
        #Cria o centralWidget da área do cliente
        self.conteudo_central = QMdiArea()
        #Difine o primeiro widget do centralWidget
        self.conteudo_central.addWidget(self.home_gerente)
        self.conteudo_central.setCurrentWidget(self.home_gerente)
    def setLayoutGerente(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_conteudo = QHBoxLayout()
        self.layout_conteudo.addWidget(self.conteudo_central)
        self.setLayout(self.layout_conteudo)
        
        
