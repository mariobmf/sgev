# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Formulario para cadastro do estoquista---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QFormLayout,
                            QLineEdit, QPushButton, QLabel, QMessageBox)
from view.BaseSubWindow import BaseSubWindow
from view.BaseFormulario import BaseFormulario
class CadastroEstoquista(BaseSubWindow):
    def __init__(self, parent=None):
        super().__init__("Cadastro do Estoquista", 300, 300)
        self.parent = parent
        self.base_form = BaseFormulario(self)
        self.setWidgets()
        self.base_form.setStyleSheetForm()
        self.setLayoutCadastro()
        self.setActionButton()
        self.base_form.connectValidaCampo()
    def setWidgets(self):
        '''Cria os Widgets da tela da área do gerente'''
        self.conteudo = QWidget()
        self.lbl_title = QLabel("DADOS DO ESTOQUISTA")
        self.lbl_title.setStyleSheet("QLabel{font:bold}")
        self.edit_cpf = QLineEdit()
        self.edit_cpf.setInputMask("999.999.999-99")
        self.edit_num_cracha = QLineEdit()
        self.edit_nome = QLineEdit()
        self.edit_sobrenome = QLineEdit()
        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.setAutoDefault(True)
    def setLayoutCadastro(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_form = QFormLayout()
        self.layout_form.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.layout_form.addRow(self.lbl_title)
        self.layout_form.addRow("CPF",self.edit_cpf)
        self.layout_form.addRow("Nº Crachá",self.edit_num_cracha)
        self.layout_form.addRow("Nome",self.edit_nome)
        self.layout_form.addRow("Sobrenome",self.edit_sobrenome)
        self.layout_form.addRow(self.btn_cadastrar)
        self.conteudo.setLayout(self.layout_form)
        self.setWidget(self.conteudo)
    def setActionButton(self):
        self.btn_cadastrar.clicked.connect(self.parent.cadastrarEstoquista)
    def showMessageSucesso(self):
        '''Exibe uma Dialog com a menssagem de sucesso ao cadastro'''
        QMessageBox.about(self,"Sucesso",
                        "Estoquista cadastrado com sucesso! Alterar a senha no primeiro login.")
    def showMessageErro(self):
        '''Exibe uma Dialog com a menssagem de Estoquista ja cadastrado'''
        QMessageBox.about(self,"Erro",
                        "CPF do Estoquista já cadastrado, verifique a lista de estoquistas cadastrados")