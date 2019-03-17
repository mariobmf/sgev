# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Lista de todos os produtos cadastrados no sistema---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QPushButton, QTableWidget, QTableWidgetItem, 
                            QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QAbstractItemView)
from PyQt5.QtGui import QIcon
from controller.Controller import Controller

class ListaProdutos(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setTable()
        self.setLayoutTable()
    def setTable(self):
        '''Cria os Widgets da tabela'''
        self.produtos = self.parent.controller.produto.getProdutos()#Pega os produtos salvos no sistema
        self.table = QTableWidget(len(self.produtos),11)#Cria a tabela com a quantidade de linhas conforme os produtos e 11 colunas
        header_label = """Ação-Código de Barras-Lote-Categoria-Nome-Descrição-Unidade-Quantidade-Peso-Local de Armazenamento-Data de Vencimento"""#Lista usada para formar os titulos da tabela
        self.table.setHorizontalHeaderLabels(header_label.split('-'))#Interpreta a lista de titulos e seta os titulos da tabela
        self.setValuesTable()#Coloca os valores na tabela
        self.table.resizeColumnsToContents()#As colunas ficam com a largura do tamanho do conteudo
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)#Bloqueia o edit nos itens 
    def setLayoutTable(self):
        '''Posiciona os Widgets da tabela'''
        self.group_box = QGroupBox("Produtos cadastrados no sistema")
        self.layout_group = QVBoxLayout()
        self.layout_lista = QVBoxLayout()
        self.layout_lista.addWidget(self.table)
        self.group_box.setLayout(self.layout_lista)
        self.layout_group.addWidget(self.group_box)
        self.setLayout(self.layout_group)
    def setValuesTable(self):
        '''Preenche a tabela usando dois laços de repetição(um para linhas e outro para colunas)'''
        linha = 0
        coluna = 1
        for produto in self.produtos:#Separa as linhas dos produtos
            self.table.setCellWidget(linha, 0, ButtonGroup(self, produto[0]))#Coloca os botões na celula e passa o id do produto
            for item in produto[1:]:#Separa cada coluna da linha(da segunda coluna em diante)
                self.table.setItem(linha, coluna, QTableWidgetItem(str(item)))
                coluna += 1
            coluna = 1
            linha += 1
class ButtonGroup(QWidget):
    def __init__(self, parent, id_produto):
        '''Cria o grupo de botões(editar e visualizar) que vão ser inseridos na primeiro coluna de cada linha'''
        super().__init__()
        self.parent = parent
        self.id_produto = id_produto
        self.btn_edit = QPushButton(QIcon("icons/pencil-edit-button.png"),"")
        self.btn_view = QPushButton(QIcon("icons/eye-button.png"),"")
        self.btn_edit.clicked.connect(self.actionButtonEdit)
        self.btn_view.clicked.connect(self.actionButtonView)
        self.layout_btn_group = QHBoxLayout()#Layout horizontal para os botões
        self.layout_btn_group.setContentsMargins(3,0,3,0)#Margem nas laterais dos botões
        self.layout_btn_group.addWidget(self.btn_edit,1)
        self.layout_btn_group.addWidget(self.btn_view,1)
        self.setLayout(self.layout_btn_group)
    def actionButtonEdit(self):
        '''Aciona o metodo editProduto e passa o id do produto'''
        self.parent.parent.controller.editProduto(self.id_produto)#primeiro parent(class ListaProdutos) e o segundo parent(AreaEstoquista)
    def actionButtonView(self):
        '''Aciona o metodo editProduto e passa o id do produto'''
        self.parent.parent.controller.viewProduto(self.id_produto)#primeiro parent(class ListaProdutos) e o segundo parent(AreaEstoquista)
