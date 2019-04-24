# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 21/04/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Base para todos os formularios do sistema---

# --- Import PyQt5
from PyQt5.QtWidgets import (QLineEdit)

class BaseFormulario():
    def __init__(self, parent):
        self.parent = parent
    def setStyleSheetForm(self):
            self.parent.setStyleSheet("""QLineEdit, QComboBox{border-radius: 3px;
                                            border-style: solid;
                                            border-width: 1px;
                                            border-color: Gray;
                                            padding: 2px}
                                QLineEdit:focus, QComboBox:focus{border-color:blue}
                                QPushButton{padding:5px}
                                QDateEdit{padding:3px}""")
    def clearLineEdit(self):
        '''Apaga todos os campos do formulario, pode ser usado para fazer um novo cadastro'''
        edits = self.parent.findChildren(QLineEdit)
        for edit in edits:
            edit.clear()
    def verificaCamposVazios(self):
        '''verifica se no formulario existem algum campo vazio
            Retorno:
                True - caso não tenha nenhum campo vazio
        '''
        edits = self.parent.findChildren(QLineEdit)
        vazio = 0
        for edit in edits:
            if(edit.text() == ""):
                edit.setStyleSheet("border-color: red")
                vazio += 1
        if(vazio > 0):
            return False
        else:
            return True
    def validaCpf(self, campo):
        if(len(campo.text()) == 14):
            return True
        else:
            campo.setStyleSheet("border-color: red")
    def validaCampo(self):
        '''Muda a cor da borda do QLineEdit se ele estiver vazio'''
        campo = self.parent.sender()
        if(campo.text() != ""):
            campo.setStyleSheet("border-color: green")
        else:
            campo.setStyleSheet("border-color: red")
    def connectValidaCampo(self):
        '''Conecta todos os campos com a função validaCampo'''
        edits = self.parent.findChildren(QLineEdit)
        for edit in edits:
            edit.textChanged.connect(self.validaCampo)