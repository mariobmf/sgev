# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 23/02/2019 - Alterado
# VERSÂO 2.0
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Janela com Formulario para troca de senha de todos usuários---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QFormLayout, 
                            QLineEdit, QPushButton, QLabel, QMessageBox)
from view.BaseSubWindow import BaseSubWindow
class TrocaSenha(BaseSubWindow):
    def __init__(self, parent=None):
        super().__init__("Troca de Senha", 250, 200)
        self.parent = parent
        self.setWidgets()
        self.setLayoutTrocaSenha()
        self.setActionButton()
    def setWidgets(self):
        '''Cria os Widgets da tela da área do gerente'''
        self.conteudo = QWidget()
        self.lbl_title = QLabel("DADOS NECESSARIOS")
        self.lbl_title.setStyleSheet("QLabel{font:bold}")
        self.edit_senha_antiga = QLineEdit()
        self.edit_senha_antiga.setEchoMode(QLineEdit.Password)
        self.edit_senha_nova = QLineEdit()
        self.edit_senha_nova.setEchoMode(QLineEdit.Password)
        self.edit_confirma_nova = QLineEdit()
        self.edit_confirma_nova.setEchoMode(QLineEdit.Password)
        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.setAutoDefault(True)
    def setLayoutTrocaSenha(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_form = QFormLayout()
        self.layout_form.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.layout_form.addRow(self.lbl_title)
        self.layout_form.addRow("Senha antiga",self.edit_senha_antiga)
        self.layout_form.addRow("Nova senha",self.edit_senha_nova)
        self.layout_form.addRow("Confirmar senha",self.edit_confirma_nova)
        self.layout_form.addRow(self.btn_salvar)
        self.conteudo.setLayout(self.layout_form)
        self.setWidget(self.conteudo)
    def setActionButton(self):
        self.btn_salvar.clicked.connect(self.parent.trocarSenha)
    def showMessageSucesso(self):
        '''Exibe uma Dialog com a menssagem de sucesso ao trocar a senha'''
        QMessageBox.about(self,"Sucesso",
                        "Senha alterada com sucesso!")
    def showMessageErro(self):
        '''Exibe uma Dialog com a menssagem de erro ao trocar a senha'''
        QMessageBox.about(self,"Erro",
                        "Erro ao trocar a senha! Verifique as informações fornecidas.")