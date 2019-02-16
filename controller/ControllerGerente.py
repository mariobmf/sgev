# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções da área do gerente---

# --- Import PyQt5
from PyQt5.QtWidgets import QWidget, QAction, QLabel, QVBoxLayout

class ControllerGerente():
    '''Todas funcções e ações da área do gerente estão nesta classe'''
    def __init__(self, parent):
        self.parent = parent
    def deconectar(self):
        '''Desconecta o usuário atual, redireciona o sistema para a tela de login'''
        self.parent.startInterfaceLogin()#Carrega a tela de Login
        self.parent.setMenus()#Configura o Menu da Tela Inicial
        