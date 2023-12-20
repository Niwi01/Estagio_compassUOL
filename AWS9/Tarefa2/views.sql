CREATE view dim_cliente as
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_cliente;


CREATE VIEW dim_carro as
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
from tb_carro

CREATE VIEW dim_combustiveis AS
SELECT idCombustivel, tipoCombustivel
FROM tb_combustiveis 


CREATE VIEW dim_vendedores AS
SELECT idVendedor,nomeVendedor,sexoVendedor,estadoVendedor
FROM tb_vendedores


CREATE VIEW fato_locacao AS
SELECT 
	idLocacao, 
	dataLocacao, 
	horaLocacao, 
	qtdDiaria, 
	vlrDiaria, 
	dataEntrega, 
	horaEntrega, 
	idCliente, 
	idCarro, 
	idCombustivel, 
	idVendedor
FROM Locacao 

select * from dim_carro
select * from dim_cliente dc
select * from dim_combustiveis dc 
select * from dim_vendedores dv 
select * from fato_locacao fl 
