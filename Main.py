# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 23/02/2019 - Alterado
# VERSÂO 2.0
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Interface principal (inicia o sistema, classe main será a base para todas as outra interfaces)---

# ---Import Pyqt5
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QAction,
                            QStackedWidget, QMdiArea, QLabel, QMessageBox, QStatusBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon 
# ---Import necessario para funcionamento do Pyqt5
import sys
# ---Import Pacotes do sistema
from controller.Usuario import Usuario
from controller.Produto import Produto
from controller.Menu import Menu
from view.Login import Login
from model.Bd import Bd
class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.screen = QApplication.primaryScreen()
        self.menu = Menu(self)
        self.startInterfaceLogin()
        self.setSettings()
        self.menu.setMenusPrincipal()
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
    def startInterfaceLogin(self):
        '''Configura o Widget central da Janela principal e Inicia as Interfaces necessarias para a tela inicial'''
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
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
        msg_sobre.setInformativeText("Versão 2.0")
        msg_sobre.setDefaultButton(QMessageBox.Ok)
        msg_sobre.exec_()
    def conectar(self):
        '''Ação do botão entrar da tela de login'''
        self.usuario = Usuario(self.formataCpf(self.login.edit_cpf.text()), self.login.edit_password.text())
        if(self.usuario.autenticaUsuario()):
            if self.usuario.id_conta == 1:
                pass
            elif self.usuario.id_conta == 2:
                from controller.ControllerGerente import ControllerGerente
                self.controller = ControllerGerente(self)
                self.menu.setMenusGerente()         
            elif self.usuario.id_conta == 3:
                from controller.ControllerEstoquista import ControllerEstoquista
                self.controller = ControllerEstoquista(self)
                self.menu.setMenusEstoquista()
            else:
                QMessageBox.warning(self, "Conta", "Conta do usuário não cadastrada", QMessageBox.Ok)
            self.mdi_area = QMdiArea()
            self.setCentralWidget(self.mdi_area)
            del self.central_widget #Deleta o centralWidget atual para inicialização da MDIArea 
            del self.login #Deleta a instancia da classe Login
        else:
            QMessageBox.warning(self, "Cliente", "Usuário não cadastrado", QMessageBox.Ok)
    def formataCpf(self, cpf):
        '''Retorna o CPF formatado(somente Numeros)
            parametros:
                cpf - Não formatado ex: 111.222.333-44
            retorno:
                cpf - Formatado ex: 11122233344'''
        cpf_formatado = ""
        for digito in str(cpf):
            if digito.isdigit():
                cpf_formatado += str(digito)
        return cpf_formatado
if __name__ == '__main__':
    #bd = Bd()
    #print(bd.connectBd())
    root = QApplication(sys.argv)
    #if(Bd().connectBd() != None):
    app = Main()
    #else:
     #   app = QWidget()
      #  erro = QMessageBox(app)
       # erro.setWindowTitle("Erro")
        #erro.setIcon(QMessageBox.Warning)
        #erro.setText("Erro com o Banco de Dados, verifique o servidor de banco de dados")
        #erro.setStandardButtons(QMessageBox.Ok)
        #app.show()
        #print("Erro com o Banco de Dados, verifique o servidor de banco de dados")
    sys.exit(root.exec_())  
