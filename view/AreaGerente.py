# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface da área do genrete (Menus da área do gerente)---

# --- Import PyQt5
from PyQt5.QtWidgets import QWidget, QAction, QLabel, QVBoxLayout
from controller.ControllerGerente import ControllerGerente

class AreaGerente(QWidget):
    '''Todos componentes graficos da área do gerente estão nesta classe'''
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.controller = ControllerGerente(self.parent)
        self.setMenus()
        self.setWidgets()
        self.setLayoutLogin()
    def setMenus(self):
        '''Altera as opções do menubar para as necessidades do gerente'''
        self.parent.main_menu.clear()
        #cria novas opções
        menu_cadastro = self.parent.main_menu.addMenu("Cadastro")
        menu_relatorios = self.parent.main_menu.addMenu("Relatórios")
        menu_sobre = self.parent.main_menu.addMenu("Sobre")
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
        act_sair.triggered.connect(self.parent.close)
        act_desconectar.triggered.connect(self.controller.deconectar)
        #-Menu de Relatórios
        act_entra_saida = QAction("Relatório de Entrada e Saída", self)
        act_perdas = QAction("Relatório de Perdas", self)
        act_total_estoque = QAction("Relatório Total de Estoque", self)
        act_vencimentos_futuros = QAction("Relatório de Vencimentos Futuros", self)
        menu_relatorios.addAction(act_entra_saida)
        menu_relatorios.addAction(act_perdas)
        menu_relatorios.addAction(act_total_estoque)
        menu_relatorios.addAction(act_vencimentos_futuros)
    def setWidgets(self):
        '''Cria os Widgets da tela da área do gerente'''
        
    def setLayoutLogin(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        
