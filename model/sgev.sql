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
CREATE TABLE IF NOT EXISTS categoriaProduto (
	id_categoria INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(50),
    tipo VARCHAR(15) NOT NULL,
    PRIMARY KEY(id_categoria),
    CONSTRAINT categoria_fk_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
);
CREATE TABLE IF NOT EXISTS produto (
	id_produto INT NOT NULL AUTO_INCREMENT,
    id_categoria INT NOT NULL,
    codigo_barras VARCHAR(30) NOT NULL,
    lote VARCHAR(30) NOT NULL,
    nome VARCHAR(30) NOT NULL,
    unidade VARCHAR(15) NOT NULL,
    quantidade INT NOT NULL,
    peso FLOAT NOT NULL,
    local_armazenamento VARCHAR(50) NOT NULL,
    data_vencimento DATE NOT NULL,
    PRIMARY KEY(id_produto),
    CONSTRAINT produto_fk_categoria FOREIGN KEY(id_categoria) REFERENCES categoriaProduto(id_categoria)
);
INSERT INTO conta (id_conta,descricao) VALUES(1,"Administrador"),(2,"Gerente"),(3,"Estoquista");
INSERT INTO usuario (	) VALUES (2,"11409036677","123456","Mário","Fernandes","123456");

SELECT * FROM usuario;