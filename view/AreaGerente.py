# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface da área do genrete (Menus da área do gerente)---

# --- Import PyQt5
from PyQt5.QtWidgets import QWidget, QAction, QStackedWidget, QHBoxLayout
#import dos controllers
from controller.ControllerGerente import ControllerGerente
#Import das View
from view.TrocaSenha import TrocaSenha
from view.CadastroEstoquista import CadastroEstoquista
from view.RelatorioSimples import RelatorioSimples
class AreaGerente(QWidget):
    '''Todos componentes graficos da área do gerente estão nesta classe'''
    def __init__(self, parent=None):
        super().__init__()
        self.main_class = parent#Variavel usada para acessar a classe principal
        self.controller = ControllerGerente(self)
        self.setCentralWidgets()
        self.setMenus()
        self.setLayoutGerente()
    def setMenus(self):
        '''Altera as opções do menubar para as necessidades do gerente'''
        self.main_class.main_menu.clear()
        #cria novas opções
        menu_cadastro = self.main_class.main_menu.addMenu("Cadastro")
        menu_relatorios = self.main_class.main_menu.addMenu("Relatórios")
        menu_sobre = self.main_class.main_menu.addMenu("Sobre")
        #---cria as ações do menu
        #-Menu de Cadastro
        act_cadastro_estoquista = QAction("Cadastrar Estoquista", self)
        act_troca_senha = QAction("Trocar Senha", self)
        act_desconectar = QAction("Desconectar", self)
        act_sair = QAction("Fechar",self)
        menu_cadastro.addAction(act_cadastro_estoquista)
        menu_cadastro.addAction(act_troca_senha)
        menu_cadastro.addAction(act_desconectar)
        menu_cadastro.addAction(act_sair)
        act_cadastro_estoquista.triggered.connect(self.controller.showCadastraEstoquista)
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
    def setCentralWidgets(self):
        '''Cria o Widget Central da tela da área do gerente'''
        #Cria os telas da área do cliente
        self.home_gerente = RelatorioSimples(self)#Um relatorio simples é usado como tela inicial
        self.cadastro_estoquista = CadastroEstoquista(self)
        self.troca_senha = TrocaSenha(self)
        #Cria o centralWidget da área do cliente
        self.conteudo_central = QStackedWidget(self)
        #Difine o primeiro widget do centralWidget
        self.conteudo_central.addWidget(self.home_gerente)
        self.conteudo_central.setCurrentWidget(self.home_gerente)
    def setLayoutGerente(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_conteudo = QHBoxLayout()
        self.layout_conteudo.addWidget(self.conteudo_central)
        self.setLayout(self.layout_conteudo)
        
        
