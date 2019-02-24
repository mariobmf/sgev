# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções da área do gerente---

from controller.Controller import Controller
from controller.Usuario import Usuario
from controller.Produto import Produto

class ControllerGerente(Controller):
    '''Todas funcções e ações da área do gerente estão nesta classe'''
    def __init__(self, parent):
        self.parent = parent# variavel usada para acessar a classe AreaGerente
        super().__init__(self.parent)
        self.produto = Produto(False)
    def showCadastraEstoquista(self):
        self.parent.conteudo_central.addWidget(self.parent.cadastro_estoquista)
        self.parent.conteudo_central.setCurrentWidget(self.parent.cadastro_estoquista)
    def cadastrarEstoquista(self):
        cpf = self.parent.cadastro_estoquista.edit_cpf.text()
        num_cracha = self.parent.cadastro_estoquista.edit_num_cracha.text()
        nome = self.parent.cadastro_estoquista.edit_nome.text()
        sobrenome = self.parent.cadastro_estoquista.edit_sobrenome.text()
        id_conta = 3#Valor padrão para uma conta do tipo Estoquista
        estoquista = Usuario(cpf, cpf, num_cracha, nome, sobrenome, id_conta)
        if(estoquista.cadastraUsuario()):
            self.parent.cadastro_estoquista.showMessageSucesso()