# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 23/02/2019 - Alterado
# VERSÂO 2.0
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Configuração dos menus---

# --- Import PyQt5
from PyQt5.QtWidgets import QAction, QMenuBar
class Menu():
    '''Todos componentes graficos da área do gerente estão nesta classe'''
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent#Variavel usada para acessar a classe principal
        self.main_menu = self.parent.menuBar()
    def setMenusPrincipal(self):
        '''Configura o menubar da tela inicial'''
        self.main_menu.clear()
        menu_arquivo = self.main_menu.addMenu("Arquivo")
        menu_sobre = self.main_menu.addMenu("Ajuda")
        act_sair = QAction("Fechar",self.parent)
        act_ajuda = QAction("Sobre", self.parent)
        act_sair.triggered.connect(self.parent.close)
        act_ajuda.triggered.connect(self.parent.showSobre)
        menu_arquivo.addAction(act_sair)
        menu_sobre.addAction(act_ajuda)
    def setMenusGerente(self):
        '''Altera as opções do menubar para as necessidades do gerente'''
        self.main_menu.clear()
        #cria novas opções
        menu_cadastro = self.main_menu.addMenu("Cadastro")
        menu_estoquista = self.main_menu.addMenu("Estoquistas")
        menu_relatorios = self.main_menu.addMenu("Relatórios")
        menu_sobre = self.main_menu.addMenu("Sobre")
        #---cria as ações do menu
        #-Menu de Cadastro
        act_troca_senha = QAction("Trocar Senha", self.parent)
        act_desconectar = QAction("Desconectar", self.parent)
        act_sair = QAction("Fechar",self.parent)
        menu_cadastro.addAction(act_troca_senha)
        menu_cadastro.addAction(act_desconectar)
        menu_cadastro.addAction(act_sair)
        act_troca_senha.triggered.connect(self.parent.controller.showTrocaSenha)
        act_desconectar.triggered.connect(self.parent.controller.deconectar)
        act_sair.triggered.connect(self.parent.close)
        #-Menu de Estoquistas
        act_cadastro_estoquista = QAction("Cadastrar Estoquista", self.parent)
        act_listar_estoquista = QAction("Listar Estoquistas", self.parent)
        menu_estoquista.addAction(act_cadastro_estoquista)
        menu_estoquista.addAction(act_listar_estoquista)
        act_cadastro_estoquista.triggered.connect(self.parent.controller.showCadastraEstoquista)

        #-Menu de Relatórios
        act_entra_saida = QAction("Relatório de Entrada e Saída", self.parent)
        act_perdas = QAction("Relatório de Perdas", self.parent)
        act_total_estoque = QAction("Relatório Total de Estoque", self.parent)
        act_vencimentos_futuros = QAction("Relatório de Vencimentos Futuros", self.parent)
        menu_relatorios.addAction(act_entra_saida)
        menu_relatorios.addAction(act_perdas)
        menu_relatorios.addAction(act_total_estoque)
        menu_relatorios.addAction(act_vencimentos_futuros)
    def setMenusEstoquista(self):
        '''Altera as opções do menubar para as necessidades do gerente'''
        self.main_menu.clear()
        #cria novas opções
        menu_cadastro = self.main_menu.addMenu("Cadastro")
        menu_relatorios = self.main_menu.addMenu("Relatórios")
        menu_produtos = self.main_menu.addMenu("Produtos")
        menu_sobre = self.main_menu.addMenu("Sobre")
        #---cria as ações do menu
        #-Menu de Cadastro
        act_troca_senha = QAction("Trocar Senha", self.parent)
        act_desconectar = QAction("Desconectar", self.parent)
        act_sair = QAction("Fechar",self.parent)
        menu_cadastro.addAction(act_troca_senha)
        menu_cadastro.addAction(act_desconectar)
        menu_cadastro.addAction(act_sair)
        act_troca_senha.triggered.connect(self.parent.controller.showTrocaSenha)
        act_desconectar.triggered.connect(self.parent.controller.deconectar)
        act_sair.triggered.connect(self.parent.close)
        #-Menu de Relatórios
        act_entra_saida = QAction("Relatório de Entrada e Saída", self.parent)
        act_perdas = QAction("Relatório de Perdas", self.parent)
        act_total_estoque = QAction("Relatório Total de Estoque", self.parent)
        act_vencimentos_futuros = QAction("Relatório de Vencimentos Futuros", self.parent)
        menu_relatorios.addAction(act_entra_saida)
        menu_relatorios.addAction(act_perdas)
        menu_relatorios.addAction(act_total_estoque)
        menu_relatorios.addAction(act_vencimentos_futuros)
        #-Menu Produtos
        act_cadastra_produto = QAction("Cadastrar Produtos", self.parent)
        act_lista_produto = QAction("Listar Produtos", self.parent)
        act_cadastra_unidade = QAction("Cadastrar Unidade", self.parent)
        act_lista_unidade = QAction("Listar Unidade", self.parent)
        act_cadastra_categoria = QAction("Cadastrar Categoria", self.parent)
        act_lista_categoria = QAction("Listar Categoria", self.parent)
        menu_produtos.addAction(act_cadastra_produto)
        menu_produtos.addAction(act_lista_produto)
        menu_produtos.addAction(act_cadastra_unidade)
        menu_produtos.addAction(act_lista_unidade)
        menu_produtos.addAction(act_cadastra_categoria)
        menu_produtos.addAction(act_lista_categoria)
        act_cadastra_produto.triggered.connect(self.parent.controller.showCadastroProduto)
        act_lista_produto.triggered.connect(self.parent.controller.showListaProdutos)