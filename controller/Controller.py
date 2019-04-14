# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 23/02/2019 - Alterado
# VERSÂO 2.0
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções comuns para todos usuários---

# ---Import Pyqt5
from PyQt5.QtWidgets import QLabel, QStatusBar
from datetime import date
# ---Import View
from view.TrocaSenha import TrocaSenha

class Controller():
    '''Todas funções e ações comuns para todos os usuários estão nesta classe'''
    def __init__(self, parent):
        self.parent = parent
        self.setStatusBar()
    def setStatusBar(self):
        '''Substitui a statuBar inicial pelo nome do usuário e data atual'''
        self.status_bar = QStatusBar(self.parent)#Cria uma nova statusBar
        self.parent.setStatusBar(self.status_bar)#Define a nova statusBar como padrão
        #Adiciona o texto do lado esquerdo da statusBar
        self.status_bar.addWidget(QLabel(str(self.parent.usuario.descricao)))
        self.status_bar.addWidget(QLabel("-"))
        self.status_bar.addWidget(QLabel(self.parent.usuario.nome))
        self.status_bar.addWidget(QLabel(self.parent.usuario.sobrenome))
        #Adiciona o texto do lado direito da statusBar
        self.status_bar.addPermanentWidget(QLabel(date.today().strftime('%d/%m/%Y')))
    def deconectar(self):
        '''Desconecta o usuário atual, redireciona o sistema para a tela de login'''
        del self.parent.usuario#Excluir a instancia da classe usuario, para ser instanciada uma nova classe em um futuro login
        self.parent.startInterfaceLogin()#Carrega a tela de Login
        self.parent.menu.setMenusPrincipal()#Configura o Menu da Tela Inicial
        del self.parent.mdi_area #Deleta o MDIArea para inicialização do centralWidget da tela de login 
    def showTrocaSenha(self):
        '''Altera o widget central para o formulario de troca de senha'''
        self.sub_troca_senha = TrocaSenha(self)
        self.parent.mdi_area.addSubWindow(self.sub_troca_senha)
        self.sub_troca_senha.show()
    def trocarSenha(self):
        '''Altera a senha do usuário'''
        senha_antiga = self.sub_troca_senha.edit_senha_antiga.text()#Recebe o valor digitado
        senha_nova = self.sub_troca_senha.edit_senha_nova.text()#Recebe o valor digitado
        confirma_nova = self.sub_troca_senha.edit_confirma_nova.text()#Recebe o valor digitado
        if(senha_nova == confirma_nova):#Compara o valor das novas senhas 
            if(senha_antiga == self.parent.usuario.password):#compara a senha antiga
                self.parent.usuario.password = senha_nova#troca a senha na instancia do objeto
                if(self.parent.usuario.alteraSenha()):#aciona o metodo do objeto para trocar a senha no banco
                    self.sub_troca_senha.showMessageSucesso()#caso a troca do banco retorne com sucesso exibe a menssagem de sucesso    
                    self.parent.mdi_area.removeSubWindow(self.sub_troca_senha)#remove a subwindow da tela
                    del self.sub_troca_senha#deleta a instancia da subwindow
            else:#Caso a senha antiga estiver errada
                self.sub_troca_senha.showMessageErro()
        else:#Caso a senha digitade esteja errada
            self.sub_troca_senha.showMessageErro()    
    def showRelatorioSimples(self):
        '''Exibe um relatorio simples no central widget determinado nos parametros
            Usado para tela home do gerente e estoquista
            Informações do relatorio:
                -Quantidade em Estoque
                -Produtos vencidos
                -Produtos que vencem em 30 dias
                -Produtos que vencem em 60 dias
        '''
        self.parent.conteudo_central.addWidget(self.home_gerente)
        self.parent.conteudo_central.setCurrentWidget(self.home_gerente)
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