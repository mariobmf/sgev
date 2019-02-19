# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções da área do gerente---

from controller.Controller import Controller
from controller.Usuario import Usuario

class ControllerGerente(Controller):
    '''Todas funcções e ações da área do gerente estão nesta classe'''
    def __init__(self, parent):
        self.area_gerente = parent# variavel usada para acessar a classe AreaGerente
        super().__init__(self.area_gerente)
    def showCadastraEstoquista(self):
        self.area_gerente.conteudo_central.addWidget(self.area_gerente.cadastro_estoquista)
        self.area_gerente.conteudo_central.setCurrentWidget(self.area_gerente.cadastro_estoquista)
    def cadastrarEstoquista(self):
        cpf = self.area_gerente.cadastro_estoquista.edit_cpf.text()
        num_cracha = self.area_gerente.cadastro_estoquista.edit_num_cracha.text()
        nome = self.area_gerente.cadastro_estoquista.edit_nome.text()
        sobrenome = self.area_gerente.cadastro_estoquista.edit_sobrenome.text()
        id_conta = 3#Valor padrão para uma conta do tipo Estoquista
        estoquista = Usuario(cpf, cpf, num_cracha, nome, sobrenome, id_conta)
        if(estoquista.cadastraUsuario()):
            self.area_gerente.cadastro_estoquista.showMessageSucesso()