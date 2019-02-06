# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface principal (inicia o sistema, classe main será a base para todas as outra interfaces)---

# ---Import Pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# ---Import necessario para funcionamento do Pyqt5
import sys
# ---Import Pacotes do sistema
from view.Login import Login
class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWidgets()
        self.startInterfaces()
        self.setSettings()
    def setSettings(self):
        self.setWindowTitle("SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO")
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowIcon(QIcon("logo.png"))
        self.show()
    def setWidgets(self):
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
    def startInterfaces(self):
        self.login = Login(self)
        self.central_widget.addWidget(self.login)
        self.central_widget.setCurrentWidget(self.login)
if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())

