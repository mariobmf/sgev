# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Relatório Simples que é exibido na tela incial do gerente e do estoquista---

# --- Import PyQt5
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from controller.Controller import Controller

class RelatorioSimples(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setWidgets()
        self.setLayoutLogin()
    def setWidgets(self):
        '''Cria os Widgets do relatorio'''
        total_produtos = self.parent.controller.produto.getTotalProdutos()
        self.total_vencidos = None
        self.total_vencidos_trinta = None
        self.total_vencidos_sessenta = None
        self.quantidade = QLabel("Quantidade em Estoque: " + str(total_produtos))
        self.vencidos = QLabel("Produtos vencidos: ")
        self.vencidos_trinta = QLabel("Produtos que vencem em 30 dias: ")
        self.vencidos_sessenta = QLabel("Produtos que vencem em 60 dias: ")
    def setLayoutLogin(self):
        '''Posiciona os Widgets do relatorio'''
        self.layout_linhas = QVBoxLayout()
        self.layout_linhas.addWidget(self.quantidade)
        self.layout_linhas.addWidget(self.vencidos)
        self.layout_linhas.addWidget(self.vencidos_trinta)
        self.layout_linhas.addWidget(self.vencidos_sessenta)
        self.setLayout(self.layout_linhas)
