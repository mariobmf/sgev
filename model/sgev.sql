DROP SCHEMA IF EXISTS sgev;
CREATE SCHEMA IF NOT EXISTS sgev;
USE sgev;

/******
CRIAÇÃO DAS TABELAS E SUAS RELAÇÕES
******/
CREATE TABLE IF NOT EXISTS conta (
	id_conta INT NOT NULL,
	descricao VARCHAR(15) NOT NULL,
    PRIMARY KEY(id_conta)
);
CREATE TABLE IF NOT EXISTS usuario (
	id_usuario INT NOT NULL AUTO_INCREMENT,
	id_conta INT NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE,
    numero_cracha VARCHAR(50) NOT NULL,
    nome VARCHAR(30) NOT NULL,
    sobrenome VARCHAR(30) NOT NULL,
    passwd VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_usuario),
    CONSTRAINT usuario_fk_conta FOREIGN KEY(id_conta) REFERENCES conta(id_conta)
);
CREATE TABLE IF NOT EXISTS categoria (
	id_categoria INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(50),
    tipo VARCHAR(15) NOT NULL,
    PRIMARY KEY(id_categoria),
    CONSTRAINT categoria_fk_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
);
CREATE TABLE IF NOT EXISTS unidade (
	id_unidade INT NOT NULL AUTO_INCREMENT,
    sigla VARCHAR(10) NOT NULL,
    descricao VARCHAR(30) NOT NULL,
    PRIMARY KEY(id_unidade)
);
CREATE TABLE IF NOT EXISTS produto (
	id_produto INT NOT NULL AUTO_INCREMENT,
    id_categoria INT NOT NULL,
    id_unidade INT NOT NULL,
    codigo_barras VARCHAR(100) NOT NULL,
    lote VARCHAR(30) NOT NULL,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    quantidade FLOAT NOT NULL,
    peso FLOAT NOT NULL,
    local_armazenamento VARCHAR(50) NOT NULL,
    data_vencimento DATE NOT NULL,
    PRIMARY KEY(id_produto),
    CONSTRAINT produto_fk_categoria FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria),
    CONSTRAINT produto_fk_unidade FOREIGN KEY(id_unidade) REFERENCES unidade(id_unidade)
);
INSERT INTO conta (id_conta,descricao) VALUES(1,"Administrador"),(2,"Gerente"),(3,"Estoquista");
INSERT INTO usuario (id_conta,cpf,numero_cracha,nome,sobrenome,passwd) VALUES (2,"11409036677","123456","Mário","Fernandes","123456");
INSERT INTO unidade (sigla, descricao) VALUES("CX","Caixa"),
												("CT","Cartela"),
												("DZ","Duzia"),
												("g","Grama"),
												("GS","Grosa"),
												("kg",	"Kilograma"),
												("l","Litro"),
												("m","Metro"),
												("ml","Mililitro"),
												("PT","Pacote"),
												("PR","Par"),
												("PÇ","Peça"),
												("RL","Rolo"),
												("SC60","Saca 60Kg"),
												("UN","Unidade");

INSERT INTO categoria (id_usuario, nome, descricao, tipo) 
			VALUES (1, "Leite", "Leite de Caixa", "Perecível"),
					(1, "Arroz", "Fardo", "Não Perecível"),
                    (1, "Feijão", "Preto", "Não Perecível");
INSERT INTO produto (id_categoria,
					id_unidade,
                    codigo_barras,
                    lote,
                    nome,
                    descricao,
                    quantidade,
                    peso,
                    local_armazenamento,
                    data_vencimento)
				VALUES(1,
					1,
					"46579813218913132189651",
					"LT1018",
					"Leite Cooper Rita", 
					"Leite Integral 1L",
					100,
                    1,
                    "Estoque",
                    '2019-12-31');
INSERT INTO produto (id_categoria,
					id_unidade,
                    codigo_barras,
                    lote,
                    nome,
                    descricao,
                    quantidade,
                    peso,
                    local_armazenamento,
                    data_vencimento)
				VALUES(1,
					1,
					"87494545649823165",
					"LT1019",
					"Leite Ilustre", 
					"Leite Desnatado 1L",
					178,
                    1,
                    "Estoque",
                    '2019-12-31');
INSERT INTO produto (id_categoria,
					id_unidade,
                    codigo_barras,
                    lote,
                    nome,
                    descricao,
                    quantidade,
                    peso,
                    local_armazenamento,
                    data_vencimento)
				VALUES(1,
					1,
					"8949849840984064565498",
					"LT1017",
					"Leite Ilustre", 
					"Leite Desnatado 1L",
					100,
                    1,
                    "Estoque",
                    '2017-12-31');
INSERT INTO produto (id_categoria,
					id_unidade,
                    codigo_barras,
                    lote,
                    nome,
                    descricao,
                    quantidade,
                    peso,
                    local_armazenamento,
                    data_vencimento)
				VALUES(1,
					1,
					"111111111111111",
					"LT10191",
					"Leite Ilustre", 
					"Leite Desnatado 1L",
					50,
                    1,
                    "Estoque",
                    '2019-04-20'); 
SELECT * FROM produto;
DELETE FROM produto WHERE id_produto = 2;
SELECT SUM(quantidade) FROM produto WHERE (data_vencimento > NOW()) AND (data_vencimento < current_date() + interval 30 DAY)
