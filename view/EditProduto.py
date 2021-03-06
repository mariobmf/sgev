# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Formulario para edição de produto---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QFormLayout, QLineEdit, 
                            QPushButton, QLabel, QMessageBox, QComboBox, QDateEdit)
from PyQt5.QtCore import QDate, QRegExp
from PyQt5.QtGui import QRegExpValidator

from view.BaseSubWindow import BaseSubWindow

class EditProduto(BaseSubWindow):
    def __init__(self, parent, produto):
        '''Inicia a classe com os seguintes parametros:
            -parent: classe que instanciou esta classe
            -produto: Lista com as informações do produto:
            (id,codigo,lote,categoria,nome,descricao,quantidade,unidade,peso,local,datavencimento)'''
        super().__init__("Alterar Produto",300)
        self.parent = parent
        self.produto = produto
        self.categorias = self.parent.categoria.getCategorias()
        self.unidades = self.parent.unidade.getUnidades()
        self.setWidgets()
        self.setStyleSheetForm()
        self.setLayoutEdit()
        self.setActionButton()
        self.connectValidaCampo()
    def setWidgets(self):
        '''Cria os Widgets da tela da área do gerente'''
        self.conteudo = QWidget()
        self.lbl_title = QLabel("DADOS DO PRODUTO")
        self.lbl_title.setStyleSheet("QLabel{font:bold}")
        self.edit_codigo = QLineEdit()
        self.edit_codigo.setValidator(QRegExpValidator(QRegExp("[0-9]{1,99}")))#Valida Numeros inteiros no min 1 digito e no max 99
        self.edit_codigo.setText(self.produto[1])
        self.edit_lote = QLineEdit()
        self.edit_lote.setText(self.produto[2])
        #Cria o selectbox e insere os valores do banco de dados no mesmo
        self.cb_categoria = QComboBox()
        for id_categoria, categoria in self.categorias:
            self.cb_categoria.addItem(categoria,id_categoria)
        self.cb_categoria.setCurrentText(self.produto[3])
        self.edit_nome = QLineEdit()
        self.edit_nome.setText(self.produto[4])
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setText(self.produto[5])
        self.edit_quantidade = QLineEdit()
        self.edit_quantidade.setValidator(QRegExpValidator(QRegExp("\-?\d+\.\d+")))
        self.edit_quantidade.setText(str(self.produto[6]))
        self.cb_unidade = QComboBox()
        #Cria o selectbox e insere os valores do banco de dados no mesmo
        for id_unidade, unidade in self.unidades:
            self.cb_unidade.addItem(unidade, id_unidade)
        self.cb_unidade.setCurrentText(self.produto[7])
        self.edit_peso = QLineEdit()
        self.edit_peso.setValidator(QRegExpValidator(QRegExp("\-?\d+\.\d+")))
        self.edit_peso.setText(str(self.produto[8]))
        self.edit_local = QLineEdit()
        self.edit_local.setText(self.produto[9])
        self.edit_data = QDateEdit(QDate.currentDate())
        self.edit_data.setDisplayFormat("yyyy/MM/dd")
        self.edit_data.setCalendarPopup(True)
        self.edit_data.setDate(self.produto[10])
        self.btn_cadastrar = QPushButton("Salvar")
        self.btn_cadastrar.setAutoDefault(True)
    def setStyleSheetForm(self):
        self.setStyleSheet("""QLineEdit, QComboBox{border-radius: 3px;
                                        border-style: solid;
                                        border-width: 1px;
                                        border-color: Gray;
                                        padding: 2px}
                            QLineEdit:focus, QComboBox:focus{border-color:blue}
                            QPushButton{padding:5px}
                            QDateEdit{padding:3px}""")
    def setLayoutEdit(self):
        '''Posiciona os Widgets da tela da área do gerente'''
        self.layout_form = QFormLayout()
        self.layout_form.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.layout_form.addRow(self.lbl_title)
        self.layout_form.addRow("Código de Barras",self.edit_codigo)
        self.layout_form.addRow("Lote",self.edit_lote)
        self.layout_form.addRow("Categoria",self.cb_categoria)
        self.layout_form.addRow("Nome",self.edit_nome)
        self.layout_form.addRow("Descriçao",self.edit_descricao)
        self.layout_form.addRow("Quantidade",self.edit_quantidade)
        self.layout_form.addRow("Unidade",self.cb_unidade)
        self.layout_form.addRow("Peso(kg)",self.edit_peso)
        self.layout_form.addRow("Local de Armazenamento",self.edit_local)
        self.layout_form.addRow("Data de Vencimento",self.edit_data)
        self.layout_form.addRow(self.btn_cadastrar)
        self.conteudo.setLayout(self.layout_form)
        self.setWidget(self.conteudo)
    def setActionButton(self):
        self.btn_cadastrar.clicked.connect(self.parent.editarProduto)
    def showMessageSucesso(self):
        '''Exibe uma Dialog com a menssagem de sucesso na edição'''
        result = QMessageBox.information(self,"Sucesso","Produto alterado com sucesso!")
    def clearLineEdit(self):
        '''Apaga todos os campos do formulario, pode ser usado para fazer um novo cadastro'''
        edits = self.findChildren(QLineEdit)
        for edit in edits:
            edit.clear()
    def verificaCamposVazios(self):
        '''verifica se no formulario existem algum campo vazio
            Retorno:
                True - caso não tenha nenhum campo vazio
        '''
        edits = self.findChildren(QLineEdit)
        vazio = 0
        for edit in edits:
            if(edit.text() == ""):
                edit.setStyleSheet("border-color: red")
                vazio += 1
        if(vazio > 0):
            return False
        else:
            return True
    def validaCampo(self):
        '''Muda a cor da borda do QLineEdit se ele estiver vazio'''
        campo = self.sender()
        if(campo.text() != ""):
            campo.setStyleSheet("border-color: green")
        else:
            campo.setStyleSheet("border-color: red")
    def connectValidaCampo(self):
        '''Conecta todos os campos com a função validaCampo'''
        edits = self.findChildren(QLineEdit)
        for edit in edits:
            edit.textChanged.connect(self.validaCampo)