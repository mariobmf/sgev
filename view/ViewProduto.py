# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 06/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Formulario com informações do produto---

# --- Import PyQt5
from PyQt5.QtWidgets import (QWidget, QFormLayout, QLineEdit, 
                            QPushButton, QLabel, QMessageBox, QDateEdit)

from view.BaseSubWindow import BaseSubWindow

class ViewProduto(BaseSubWindow):
    def __init__(self, parent, produto):
        '''Inicia a classe com os seguintes parametros:
            -parent: classe que instanciou esta classe
            -produto: Lista com as informações do produto:
            (id,codigo,lote,categoria,nome,descricao,quantidade,unidade,peso,local,datavencimento)'''
        super().__init__("",300)
        self.parent = parent
        self.produto = produto
        self.categorias = self.parent.categoria.getCategorias()
        self.unidades = self.parent.unidade.getUnidades()
        self.setWidgets()
        self.setStyleSheetForm()
        self.setLayoutView()
        self.setEditReadOnly()
    def setWidgets(self):
        '''Cria os Widgets da tela da área do gerente'''
        self.conteudo = QWidget()
        self.lbl_title = QLabel("DADOS DO PRODUTO")
        self.lbl_title.setStyleSheet("QLabel{font:bold}")
        self.edit_codigo = QLineEdit()
        self.edit_codigo.setText(self.produto[1])
        self.edit_lote = QLineEdit()
        self.edit_lote.setText(self.produto[2])
        self.cb_categoria = QLineEdit()
        self.cb_categoria.setText(self.produto[3])
        self.edit_nome = QLineEdit()
        self.edit_nome.setText(self.produto[4])
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setText(self.produto[5])
        self.edit_quantidade = QLineEdit()
        self.edit_quantidade.setText(str(self.produto[6]))
        self.cb_unidade = QLineEdit()
        self.cb_unidade.setText(self.produto[7])
        self.edit_peso = QLineEdit()
        self.edit_peso.setText(str(self.produto[8]))
        self.edit_local = QLineEdit()
        self.edit_local.setText(self.produto[9])
        self.edit_data = QLineEdit()
        self.edit_data.setText(str(self.produto[10]))    
    def setStyleSheetForm(self):
        self.setStyleSheet("""QLineEdit, QComboBox{border-radius: 3px;
                                        border-style: solid;
                                        border-width: 1px;
                                        border-color: Gray;
                                        padding: 2px}
                            QLineEdit:focus, QComboBox:focus{border-color:blue}
                            QPushButton{padding:5px}
                            QDateEdit{padding:3px}""")
    def setLayoutView(self):
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
        self.conteudo.setLayout(self.layout_form)
        self.setWidget(self.conteudo)
    def setEditReadOnly(self):
        '''Conecta todos os campos com a função validaCampo'''
        edits = self.findChildren(QLineEdit)
        for edit in edits:
            edit.setReadOnly(True)