# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Lista de todos as unidades cadastrados no sistema---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QPushButton, QTableWidget, QTableWidgetItem, 
                            QVBoxLayout, QHBoxLayout, QLabel, QAbstractItemView)
from PyQt5.QtGui import QIcon
from controller.Controller import Controller
from view.BaseSubWindow import BaseSubWindow

class ListaUnidade(BaseSubWindow):
    def __init__(self, parent=None):
        super().__init__("Produtos cadastrados no sistema")
        self.parent = parent
        self.setTable()
        self.setLayoutTable()
        super().setMinimumWidth(1050)
        super().setMinimumHeight(500)
    def setTable(self):
        '''Cria os Widgets da tabela'''
        self.produtos = self.parent.produto.getProdutos()#Pega os produtos salvos no sistema
        self.table = QTableWidget(len(self.produtos),11)#Cria a tabela com a quantidade de linhas conforme os produtos e 11 colunas
        header_label = """Ação-Código de Barras-Lote-Categoria-Nome-Descrição-Unidade-Quantidade-Peso(Kg)-Local de Armazenamento-Data de Vencimento"""#Lista usada para formar os titulos da tabela
        self.table.setHorizontalHeaderLabels(header_label.split('-'))#Interpreta a lista de titulos e seta os titulos da tabela
        self.setValuesTable()#Coloca os valores na tabela
        self.table.resizeColumnsToContents()#As colunas ficam com a largura do tamanho do conteudo
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)#Bloqueia o edit nos itens 
    def setLayoutTable(self):
        '''Posiciona os Widgets da tabela'''
        self.conteudo = QWidget()
        self.layout_group = QVBoxLayout()
        self.layout_group.addWidget(self.table)
        self.conteudo.setLayout(self.layout_group)
        self.setWidget(self.conteudo)
    def setValuesTable(self):
        '''Preenche a tabela usando dois laços de repetição(um para linhas e outro para colunas)'''
        linha = 0
        coluna = 1
        for produto in self.produtos:#Separa as linhas dos produtos
            self.table.setCellWidget(linha, 0, ButtonGroup(self, produto[0], linha))#Coloca os botões na celula e passa o id do produto
            for item in produto[1:]:#Separa cada coluna da linha(da segunda coluna em diante)
                self.table.setItem(linha, coluna, QTableWidgetItem(str(item)))
                coluna += 1
            coluna = 1
            linha += 1
    def updateTable(self):
        '''Atualiza as linhas da tabela'''
        self.produtos = self.parent.produto.getProdutos()#Pega os produtos salvos no sistema
        self.table.clearContents()
        if(len(self.produtos) > self.table.rowCount()):
            self.table.insertRow(int(len(self.produtos) - self.table.rowCount()))
        elif(len(self.produtos) < self.table.rowCount()):
            self.table.removeRow(int(self.table.rowCount() - len(self.produtos)))
        self.setValuesTable()
#------Classe usada para gerar dois botões dentro de uma celula------
class ButtonGroup(QWidget):
    def __init__(self, parent, id_produto, linha):
        '''Cria o grupo de botões(editar e visualizar) que vão ser inseridos na primeiro coluna de cada linha'''
        super().__init__()
        self.parent = parent
        self.id_produto = id_produto
        self.linha = linha
        self.setStyleSheet("QPushButton {border: 0px}")
        self.btn_edit = QPushButton(QIcon("icons/pencil-edit-button.png"),"")
        self.btn_view = QPushButton(QIcon("icons/eye-button.png"),"")
        self.btn_delete = QPushButton(QIcon("icons/delete-button.png"),"")
        self.btn_edit.clicked.connect(self.actionButtonEdit)
        self.btn_view.clicked.connect(self.actionButtonView)
        self.btn_delete.clicked.connect(self.actionButtonDelete)
        self.layout_btn_group = QHBoxLayout()#Layout horizontal para os botões
        self.layout_btn_group.setContentsMargins(3,0,3,0)#Margem nas laterais dos botões
        self.layout_btn_group.addWidget(self.btn_edit,1)
        self.layout_btn_group.addWidget(self.btn_view,1)
        self.layout_btn_group.addWidget(self.btn_delete,1)
        self.setLayout(self.layout_btn_group)
    def actionButtonEdit(self):
        '''Aciona o metodo editProduto e passa o id do produto'''
        #print("Id:",self.id_produto," Linha:",self.linha)
        self.parent.parent.editProduto(self.id_produto)#primeiro parent(class ListaProdutos) e o segundo parent(AreaEstoquista)
    def actionButtonView(self):
        '''Aciona o metodo viewProduto e passa o id do produto'''
        #print("Id:",self.id_produto," Linha:",self.linha)
        self.parent.parent.viewProduto(self.id_produto)#primeiro parent(class ListaProdutos) e o segundo parent(AreaEstoquista)
    def actionButtonDelete(self):
        '''Aciona o metodo deleteProduto e passa o id do produto'''
        self.parent.parent.deleteProduto(self.id_produto)#primeiro parent(class ListaProdutos) e o segundo parent(AreaEstoquista)
        