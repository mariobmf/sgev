# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Formulario para cadastro do estoquista---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QFormLayout, QHBoxLayout, 
                            QLineEdit, QPushButton, QGroupBox, QLabel, QMessageBox, QStyle)
from PyQt5.QtGui import QIcon


class CadastroEstoquista(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.width = self.parent.main_class.geometry().width()#usada para calcular a margem
        self.setWidgets()
        self.setLayoutCadastro()
        self.setActionButton()
    def setWidgets(self):
        '''Cria os Widgets da tela da área do gerente'''
        self.group_form = QGroupBox("Cadastro do Estoquista")
        self.lbl_title = QLabel("DADOS DO ESTOQUISTA")
        self.lbl_title.setStyleSheet("QLabel{font:bold}")
        self.edit_cpf = QLineEdit()
        self.edit_num_cracha = QLineEdit()
        self.edit_nome = QLineEdit()
        self.edit_sobrenome = QLineEdit()
        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.setAutoDefault(True)
    def setLayoutCadastro(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_form = QFormLayout()
        self.layout_form.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.layout_form.setContentsMargins(self.width*0.4, 100, self.width*0.4, 0)
        self.layout_form.addRow(self.lbl_title)
        self.layout_form.addRow("CPF",self.edit_cpf)
        self.layout_form.addRow("Nº Crachá",self.edit_num_cracha)
        self.layout_form.addRow("Nome",self.edit_nome)
        self.layout_form.addRow("Sobrenome",self.edit_sobrenome)
        self.layout_form.addRow(self.btn_cadastrar)
        self.group_form.setLayout(self.layout_form)
        self.layout_conteudo = QHBoxLayout()
        self.layout_conteudo.addWidget(self.group_form)
        self.setLayout(self.layout_conteudo)
    def setActionButton(self):
        self.btn_cadastrar.clicked.connect(self.parent.controller.cadastrarEstoquista)
    def showMessageSucesso(self):
        '''Exibe uma Dialog com a menssagem de sucesso ao cadastro'''
        QMessageBox.about(self,"Sucesso",
                        "Estoquista cadastrado com sucesso! Alterar a senha no primeiro login.")