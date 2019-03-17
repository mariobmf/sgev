# -*- coding: utf-8 -*-
# Autor: Mário Fernandes
# 12/02/2019
# SISTEMA DE GESTÃO DE ESTOQUE E VENCIMENTO
# ---Classe Produto---

# ---Import Pacotes do sistema
from model.Bd import Bd
from controller.Categoria import Categoria
from controller.Unidade import Unidade
class Produto():
    def __init__(self, id_produto=None, id_categoria=None, id_unidade=None, codigo_barras=None, lote=None,
                nome=None, descricao_produto=None, quantidade=None, peso=None, local_armazenamento=None, data_vencimento=None):
        '''Construtor da Classe, Iniciar o construtor das seguintes maneiras:
        -Produto(id_produto=int) = Quando for preciso consultar ou modificar um produto especifico
        -Produto(id_produto=None, id_categoria, id_unidade, codigo_barras, lote, nome, descricao_produto, quantidade, peso, 
                local_armazenamento, data_vencimento) = Quando for cadastrar um produto
        -Produto(id_produto=False) = Quando for fazer uma consulta em todos produtos'''
        self.id_produto = id_produto
        self.codigo_barras = codigo_barras
        self.lote = lote
        self.nome = nome
        self.descricao_produto = descricao_produto
        self.quantidade = quantidade
        self.peso = peso
        self.local_armazenamento = local_armazenamento
        self.data_vencimento = data_vencimento
        self.bd = Bd()
        if(self.id_produto == None):
            self.categoria = Categoria(id_categoria)
            self.unidade = Unidade(id_unidade)
        elif(self.id_produto != False):
            result = self.setDadosProduto()
    def cadastraProduto(self):
        '''Cadastra um novo produto no banco de dados'''
        try:
            con = self.bd.connectBd()
            cursor = con.cursor()
            values = (self.categoria.id_categoria, self.unidade.id_unidade, self.codigo_barras, self.lote, self.nome, 
                        self.descricao_produto, self.quantidade, self.peso, self.local_armazenamento, self.data_vencimento)
            cursor.execute("""INSERT INTO produto (id_categoria,
                                                    id_unidade,
                                                    codigo_barras,
                                                    lote,
                                                    nome,
                                                    descricao,
                                                    quantidade,
                                                    peso,
                                                    local_armazenamento,
                                                    data_vencimento) 
                                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",values)
            con.commit()
            return True
        except Exception as error:
            print("Erro: %s" % error)
        finally:
            if "con" in locals():
                con.close()
    def alteraProduto(self):
        pass
    def deletaProduto(self):
        pass
    def setDadosProduto(self):
        '''Busca os dados do produto no banco de dados e passa esses dados para a instancia do objeto'''
        con = self.bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT id_categoria, id_unidade, codigo_barras, lote, nome, descricao, quantidade, peso, local_armazenamento, data_vencimento 
                        FROM produto WHERE id_produto=%s LIMIT 1""",(self.id_produto,))
        result = cursor.fetchone()
        con.close()
        self.categoria = Categoria(result[0])
        self.unidade = Unidade(result[1])
        self.codigo_barras = result[2]
        self.lote = result[3]
        self.nome = result[4]
        self.descricao_produto = result[5]
        self.quantidade = result[6]
        self.peso = result[7]
        self.local_armazenamento = result[8]
        self.data_vencimento = result[9]
    def getTotalProdutos(self):
        '''Retorna o total de produtos cadastrado no estoque'''
        con = self.bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT SUM(quantidade) FROM produto""")
        result = cursor.fetchone()
        con.close()
        return result[0]
    def getProdutosVencidos(self):
        '''Retorna o total de produtos vencidos no estoque'''
        con = self.bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT SUM(quantidade) FROM produto WHERE data_vencimento < NOW()""")
        result = cursor.fetchone()
        con.close()
        return result[0]
    def getVencimentosProximos(self, qtd_dias):
        '''Retorna o total de produtos que vencem nos proximos dias
            - Informar a quantidade de dias para pesquisa'''
        con = self.bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT SUM(quantidade) FROM produto 
                        WHERE (data_vencimento > NOW()) 
                            AND (data_vencimento < current_date() + interval %s DAY)""",(qtd_dias,))
        result = cursor.fetchone()
        con.close()
        return result[0]
    def getProdutos(self):
        '''Retorna a lista com todos os produtos salvos no banco de dados
            Retorno:
               id_categoria,id_unidade,codigo_barras,lote,nome,descricao,quantidade,peso,local_armazenamento,data_vencimento 
        '''
        con = self.bd.connectBd()
        cursor = con.cursor()
        cursor.execute("""SELECT id_produto,codigo_barras,lote,
                                id_categoria,nome,
                                descricao,id_unidade,
                                quantidade,peso,
                                local_armazenamento,
                                data_vencimento FROM produto""")        
        result = cursor.fetchall()
        con.close()
        return result