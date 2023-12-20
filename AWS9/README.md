# RELATÓRIO DA SPRINT 9

## Tarefa 1
O objetivo da modelagem de dados é, primeiramente, organizar os dados presentes na tabela tb_locacao. Criaremos tarefas separadas que possui informações ligadas. Comecei a usar o comando CREATE TABLE em cada tabela correspondente e após isso, usar o INSERT INTO para atribuir os valores da tabela original para a tabela criada. Aqui demonstra um dos create table e inserto into:
![criandotabela](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa1/registro/criandotabela.png)
![inseredados](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa1/registro/inseredados.png)

Na criação da tabela Carros, houve um erro sobre duplicação de valores presente na coluna id na tabela de origem no momento de transferir os dados, para resolver, foi necessário criar uma tabela temporária para poder agrupar os valores, pois essa tabela tem maior facilidade de manipulação de dados antes de conseguir inserir os dados na tabela desejada:
![tabelatemporaria](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa1/registro/tabelatemporaria.PNG)
Partimos, assim, para criação da última tabela que envolve a criação de várias colunas que se referem as colunas das outras tabelas, as chaves estrangeiras.
![ultima_parte](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa1/registro/ultima_parte.PNG)

## Tarefa 2
O objetivo é montar um modelo dimensional através do modelo relacional. Então, criamos views com as mesmas informações das tabelas do modelo relacional criadas anteriormente e, assim, formamos a tabela fato, que contém o id das tabelas dimensões, e as tabelas dimensões com informações separadas.
![tarefa2](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa2/tarefa2.png)

## Tarefa 3
No primeiro job, definimos no lado do parâmetro 'JOB_NAME' os parâmetros sobre onde o arquivo csv solicitado está localizado e mais um parâmetro para indicar para onde os arquivos devem ser enviados, já convertendo-os em parquet. Os parâmetros foram definidos em "job details". Lemos o arquivo csv usando o método "glueContext.create_dynamic_frame.from_options()" e, após isso, usamos o método "glueContext.write_dynamic_frame.from_options()" para escrever em formato parquet.
![primeirojob](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa3/registro/job-resul1.png)
O mesmo acontece com o segundo job, só que convertendo json para parquet e fazemos a leitura de forma diferente dessa vez usando a função "spark.read.option()" para ler o arquivo json e a método "df.write.parquet()" para gravar o arquivo em parquet.
![segundojob](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa3/registro/job-resul2.png)

## Tarefa 4
Após criar as tabelas através do Crawlers, prossigo na aws athena para criar a tabela refinada. Fazemos a consulta usando JOIN para agrupar todas as tabelas recém criadas, selecionamos todas colunas e renomeamos algumas para não dar conflito, usamos a função CAST para fazer a conversão do tipo de dados e a cláusula CASE para verificar se o valor das colunas tem "\N" para atribuir o valor nulo a elas para, assim, evitar o impedimento de conversão de STRING para INT.
![CREATETABLE](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa4/registro/CREATETABLE.png)

Usamos os select para criar tabelas com a função de fazer modelagens solicitados:
Neste select, usei a função "CONCAT" para agrupar as colunas ID em uma só coluna.
![selectviewFILME](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa4/registro/selectviewFILME.png)

![selectAVALIACAO](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa4/registro/viewAVALIACAO.png)


E por fim:

![selectviewARTISTA](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa4/registro/selectviewARTISTA.png)

## Tarefa 5
Nessa última parte, fazemos o uso do método "glueContext.create_dynamic_frame.from_catalog()" para ler os dados da tabela da AWS Athena sem precisar usar o caminho do S3 dentro da variável "df" que lê o banco de dados e a tabela escolhido. E, finalmente, usamos o método "glueContext.write_dynamic_frame.from_options()" para especificar o tipo de conexão "s3" e o caminho que devem ser armazenados no s3 e o formato escolhido para armazenar é o parquet.
![jobtarefa5](https://github.com/Niwi01/AWS9/blob/master/Tarefas/Tarefa5/jobtarefa5.png)