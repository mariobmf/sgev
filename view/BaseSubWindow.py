# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 23/02/2019 - Alterado
# VERSÂO 2.0
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Base para as MDISubWindow que serão chamadas no sistema---

# ---Import Pyqt5
from PyQt5.QtWidgets import QMdiSubWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class BaseSubWindow(QMdiSubWindow):
    def __init__(self, title, width=None, height=None, full_screen=None):
        '''Classe base para as subjanelas usadas no sistema, nesta classe são definidos titulo, largura e altura
            Parametros:
                title = str
                width = number
                height = number
                full_screen = boolean
        '''
        super().__init__(None,Qt.WindowCloseButtonHint)
        self.setWindowTitle(title)
        if(width != None):
            self.setMaximumWidth(width)
        if(height != None):
            self.setMaximumHeight(height)
        self.setWindowIcon(QIcon("logo.png"))
        if(full_screen):
            self.showMaximized()

