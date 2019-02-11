# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface principal (inicia o sistema, classe main será a base para todas as outra interfaces)---

# ---Import Pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QSizePolicy, QLabel 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QScreen
# ---Import necessario para funcionamento do Pyqt5
import sys
# ---Import Pacotes do sistema
from view.Login import Login
class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.screen = QApplication.primaryScreen()
        self.setWidgets()
        self.startInterfaces()
        self.setSettings()
    def setSettings(self):
        self.setWindowTitle("SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO")
        self.setMinimumSize(self.screen.geometry().width()-50,self.screen.geometry().height()-50)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowIcon(QIcon("logo.png"))
        lbl_status1 = QLabel("Bem Vindo")
        lbl_status2 = QLabel("Versão 1.0")
        self.statusBar().addWidget(lbl_status1)
        self.statusBar().addPermanentWidget(lbl_status2)#showMessage("Bem Vindo")
        self.show()
    def setWidgets(self):
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.centralWidget
    def startInterfaces(self):
        self.login = Login(self)
        self.central_widget.addWidget(self.login)
        self.central_widget.setCurrentWidget(self.login)
if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())

