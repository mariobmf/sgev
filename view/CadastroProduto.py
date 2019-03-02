# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Formulario para cadastro de produto---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QFormLayout, QHBoxLayout, QLineEdit, 
                            QPushButton, QGroupBox, QLabel, QMessageBox, QComboBox, QDateEdit)
from PyQt5.QtCore import QDate
class CadastroProduto(QWidget):
    def __init__(self, parent=None, categorias=None, unidades=None):
        '''Inicia a classe com os seguintes parametros:
            -parent: classe que instanciou esta classe'''
        super().__init__()
        self.parent = parent
        self.width = self.parent.main_class.geometry().width()#usada para calcular a margem
        self.categorias = self.parent.controller.categoria.getCategorias()
        self.unidades = self.parent.controller.unidade.getUnidades()
        self.setWidgets()
        self.setLayoutCadastro()
        self.setActionButton()
    def setWidgets(self):
        '''Cria os Widgets da tela da área do gerente'''
        self.group_form = QGroupBox("Cadastro de Produto")
        self.lbl_title = QLabel("DADOS DO PRODUTO")
        self.lbl_title.setStyleSheet("QLabel{font:bold}")
        
        self.edit_codigo = QLineEdit()
        self.edit_lote = QLineEdit()
        self.cb_categoria = QComboBox()
        for id_categoria, categoria in self.categorias:
            self.cb_categoria.addItem(categoria,id_categoria)
        self.edit_nome = QLineEdit()
        self.edit_descricao = QLineEdit()
        self.edit_quantidade = QLineEdit()
        self.cb_unidade = QComboBox()
        for id_unidade, unidade in self.unidades:
            self.cb_unidade.addItem(unidade, id_unidade)
        self.edit_peso = QLineEdit()
        self.edit_local = QLineEdit()
        self.edit_data = QDateEdit(QDate.currentDate())
        self.edit_data.setDisplayFormat("yyyy/MM/dd")
        self.edit_data.setCalendarPopup(True)
        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.setAutoDefault(True)
    def setLayoutCadastro(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_form = QFormLayout()
        self.layout_form.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.layout_form.setContentsMargins(self.width*0.4, 100, self.width*0.4, 0)
        self.layout_form.addRow(self.lbl_title)
        self.layout_form.addRow("Código de Barras",self.edit_codigo)
        self.layout_form.addRow("Lote",self.edit_lote)
        self.layout_form.addRow("Categoria",self.cb_categoria)
        self.layout_form.addRow("Nome",self.edit_nome)
        self.layout_form.addRow("Descriçao",self.edit_descricao)
        self.layout_form.addRow("Quantidade",self.edit_quantidade)
        self.layout_form.addRow("Unidade",self.cb_unidade)
        self.layout_form.addRow("Peso",self.edit_peso)
        self.layout_form.addRow("Local de Armazenamento",self.edit_local)
        self.layout_form.addRow("Data de Vencimento",self.edit_data)
        self.layout_form.addRow(self.btn_cadastrar)
        self.group_form.setLayout(self.layout_form)
        self.layout_conteudo = QHBoxLayout()
        self.layout_conteudo.addWidget(self.group_form)
        self.setLayout(self.layout_conteudo)
    def setActionButton(self):
        self.btn_cadastrar.clicked.connect(self.parent.controller.cadastrarProduto)
        pass
    def showMessageSucesso(self):
        '''Exibe uma Dialog com a menssagem de sucesso ao cadastro'''
        result = QMessageBox.question(self,"Sucesso",
                        "Produto cadastrado com sucesso! \nCadastrar novo produto?", QMessageBox.Yes, QMessageBox.No)
        if(result):
            edits = self.findChildren(QLineEdit)
            for edit in edits:
                edit.clear()
        else:
            self.parent.controller.showHome()