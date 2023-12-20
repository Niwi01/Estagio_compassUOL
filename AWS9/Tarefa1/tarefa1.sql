--criando tabela
CREATE TABLE tb_cliente (
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR(100),
	cidadeCliente VARCHAR(40),
	estadoCliente VARCHAR(40),
	paisCliente VARCHAR(40)
	);

--criando tabela
CREATE TABLE tb_carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES tb_combustiveis(idCombustivel)
);

--criando tabela 
CREATE TABLE tb_vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

--criando tabela
CREATE TABLE tb_combustiveis (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

--inserindo valores da tabela cliente
-- usa-se DISTINCT para que eu consiga remover valores repetidos
INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao

--criar a tabela tb_carro não deu certo, então criaremos uma tabela temporaria:
CREATE TEMPORARY TABLE temp_carro (
  idCarro INT PRIMARY KEY,
  kmCarro INT,
  classiCarro VARCHAR(50),
  marcaCarro VARCHAR(80),
  modeloCarro VARCHAR(80),
  anoCarro INT,
  idCombustivel INT
);

--atribuindo dados
INSERT INTO temp_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao
GROUP BY idCarro;

--verificando os dados na tabela temporaria
SELECT * from temp_carro

--colocando dados da tabela temporaria na nova tabela, a tb_carro
INSERT INTO tb_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM temp_carro;

--verificando tabela
SELECT * FROM tb_carro


--inserindo dados na tabela combustivel
INSERT INTO tb_combustiveis (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao 


--parte para verificação de cada tabela
SELECT * FROM tb_cliente 
SELECT * FROM tb_carro 
SELECT * FROM tb_combustiveis 
SELECT * FROM tb_vendedores 
SELECT * FROM tb_locacao

--inserindo dados na nova tabela tb_vendedores
INSERT INTO tb_vendedores (idVendedor,nomeVendedor,sexoVendedor,estadoVendedor)
SELECT DISTINCT idVendedor,nomeVendedor,sexoVendedor,estadoVendedor
FROM tb_locacao 

--agora, na criação da tabela Locação, será colocado várias colunas como chaves estrangeiras
--isso busca eliminar dependência transitivo, evitando duplicação
CREATE TABLE Locacao (
idLocacao INT PRIMARY KEY,
dataLocacao DATETIME,
horaLocacao TIME,
qtdDiaria INT,
vlrDiaria DECIMAL(18,2),
dataEntrega DATE,
horaEntrega TIME,
idCliente INT,
idCarro INT,
idCombustivel INT,
idVendedor INT,
FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
FOREIGN KEY (idCombustivel) REFERENCES tb_combustiveis(idCombustivel),
FOREIGN KEY (idVendedor) REFERENCES tb_vendedores(idVendedor)
);

--inserindo dados a nova tabela Locacao
INSERT INTO Locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idCarro, idCombustivel, idVendedor)
SELECT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idCarro, idCombustivel, idVendedor
FROM tb_locacao 

select * from Locacao 



