# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Funções da área do gerente---

from controller.Controller import Controller
from controller.Usuario import Usuario
from controller.Produto import Produto
from view.CadastroEstoquista import CadastroEstoquista

class ControllerGerente(Controller):
    '''Todas funcções e ações da área do gerente estão nesta classe'''
    def __init__(self, parent):
        self.parent = parent# variavel usada para acessar a classe AreaGerente
        super().__init__(self.parent)
        self.produto = Produto(False)
    def showCadastraEstoquista(self):
        self.sub_cadastro_estoquista = CadastroEstoquista(self)
        self.parent.mdi_area.addSubWindow(self.sub_cadastro_estoquista)
        self.sub_cadastro_estoquista.show()
    def cadastrarEstoquista(self):
        if(self.sub_cadastro_estoquista.base_form.verificaCamposVazios()):
            if(self.sub_cadastro_estoquista.base_form.validaCpf(self.sub_cadastro_estoquista.edit_cpf)):
                cpf = self.formataCpf(self.sub_cadastro_estoquista.edit_cpf.text())
                num_cracha = self.sub_cadastro_estoquista.edit_num_cracha.text()
                nome = self.sub_cadastro_estoquista.edit_nome.text()
                sobrenome = self.sub_cadastro_estoquista.edit_sobrenome.text()
                id_conta = 3#Valor padrão para uma conta do tipo Estoquista
                estoquista = Usuario(cpf, cpf, num_cracha, nome, sobrenome, id_conta)
                if(estoquista.cadastraUsuario()):
                    self.sub_cadastro_estoquista.showMessageSucesso()
                    self.parent.mdi_area.removeSubWindow(self.sub_cadastro_estoquista)#remove a subwindow da tela
                    del self.sub_cadastro_estoquista#deleta a instancia da subwindow
                else:
                    self.sub_cadastro_estoquista.showMessageErro()