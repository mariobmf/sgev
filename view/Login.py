# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface Login (Todos os componentes do Login estão nesta classe)---

# --- Import PyQt5
from PyQt5.QtWidgets import QWidget, QLabel, QLayout, QFormLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap

class Login(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWidgets()
        self.setLayoutLogin()
    def setWidgets(self):
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap("logo.png"))
        self.logo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.edit_cpf = QLineEdit()
        self.edit_password = QLineEdit()
        self.lbl_esqueceu_senha = QLabel("Esqueceu a senha?")
        self.btn_entrar = QPushButton("Entrar")
    def setLayoutLogin(self):
        self.layout_form = QFormLayout()
        self.layout_form.addRow(self.logo)
        self.layout_form.addRow("CPF", self.edit_cpf)
        self.layout_form.addRow("Senha", self.edit_password)
        self.layout_form.addRow("", self.lbl_esqueceu_senha)
        self.layout_form.addRow(self.btn_entrar)
        self.setLayout(self.layout_form)
