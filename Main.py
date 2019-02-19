# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface principal (inicia o sistema, classe main será a base para todas as outra interfaces)---

# ---Import Pyqt5
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction,
                            QStackedWidget, QSizePolicy, QLabel, QMessageBox, QStatusBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon #QScreen
# ---Import necessario para funcionamento do Pyqt5
import sys
# ---Import Pacotes do sistema
from controller.Usuario import Usuario
from view.Login import Login
from model.Bd import Bd
class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        bd = Bd()
        #if(Bd().connectBd()):
        self.screen = QApplication.primaryScreen()
        self.main_menu = self.menuBar()
        self.setWidgets()
        self.startInterfaceLogin()
        self.setSettings()
        self.setMenus()
        #else:
         #   QMessageBox.warning(self, "Erro", "Erro com o Banco de Dados, verifique o servidor de banco de dados", QMessageBox.Ok)
          #  self.close
    def setSettings(self):
        '''Configura a aparencia da Janela principal'''
        self.setWindowTitle("SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO")
        self.setMinimumSize(self.screen.geometry().width()-50,self.screen.geometry().height()-50)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowIcon(QIcon("logo.png"))
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.addWidget(QLabel("Bem Vindo"))
        self.status_bar.addPermanentWidget(QLabel("Versão 1.0"))
        self.show()
    def setMenus(self):
        '''Configura o menubar da tela inicial'''
        self.main_menu.clear()
        menu_arquivo = self.main_menu.addMenu("Arquivo")
        menu_sobre = self.main_menu.addMenu("Ajuda")
        act_sair = QAction("Fechar",self)
        act_ajuda = QAction("Sobre", self)
        act_sair.triggered.connect(self.close)
        act_ajuda.triggered.connect(self.showSobre)
        menu_arquivo.addAction(act_sair)
        menu_sobre.addAction(act_ajuda)
    def setWidgets(self):
        '''Configura o Widget central da Janela principal'''
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
    def startInterfaceLogin(self):
        '''Inicia as Interfaces necessarias para a tela inicial'''
        self.login = Login(self)#Instancia a classe Login com a interface
        self.central_widget.addWidget(self.login)#Adiciona a insterface no centralWidget
        self.central_widget.setCurrentWidget(self.login)#Torna a interface Principal
        self.login.btn_entrar.clicked.connect(self.conectar)#Função botão Entrar
    def showSobre(self):
        '''Exibe uma Dialog com a versão e nome do software'''
        msg_sobre = QMessageBox()
        msg_sobre.setWindowIcon(QIcon("logo.png"))
        msg_sobre.setWindowTitle("Sobre")
        msg_sobre.setText("Sistema de Gestão de Estoque e Vencimento")
        msg_sobre.setInformativeText("Versão 1.0")
        msg_sobre.setDefaultButton(QMessageBox.Ok)
        msg_sobre.exec_()
    def conectar(self):
        '''Ação do botão entrar da tela de login'''
        self.usuario = Usuario(self.login.edit_cpf.text(), self.login.edit_password.text())
        if(self.usuario.autenticaUsuario()):
            if self.usuario.id_conta == 1:
                from view.AreaAdmin import AreaAdmin
                self.rota = AreaAdmin(self)
            elif self.usuario.id_conta == 2:
                from view.AreaGerente import AreaGerente
                self.rota = AreaGerente(self)                    
            elif self.usuario.id_conta == 3:
                from view.AreaEstoquista import AreaEstoquista
                self.rota = AreaEstoquista(self)
            else:
                QMessageBox.warning(self, "Conta", "Conta do usuário não cadastrada", QMessageBox.Ok)
            self.central_widget.addWidget(self.rota)#Adiciona o widget no centralWidget
            self.central_widget.setCurrentWidget(self.rota)#Torna o widget principal
            self.central_widget.removeWidget(self.login)#remove o widget Login
            del self.login #Deleta a instancia da classe Login
        else:
            QMessageBox.warning(self, "Cliente", "Usuário não cadastrado", QMessageBox.Ok)
    
if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
