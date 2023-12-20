## Relatório da Sprint 8
Aqui onde descrevo as atividades realizadas e as principais aprendizagens adquiridas ao longo da sprint.

### Atividades realizadas
* Tarefa 1

Inicialmente, criei uma conta no site themoviedb.org e, então, obtive a chave de API fornecida pelo site. Após isso, inseri a chave no código passada na questão, colocando o valor na variável "api_key". Assim, autenticando e acessando os dados do site. Com a chave no código, executei o código e tive os dados dos filmes mais bem avaliados.

* Tarefa 2

O tema que escolhi foi: Filmes de aventura populares com nota média baixa.
Defini as configurações para acessar o serviço S3, colocando as chaves de acesso e a região. Especifico o caminho do arquivo CSV a ser lido no S3. Baixo o arquivo CSV do S3 para o diretório temporário "/tmp/". Então, abro o arquivo CSV para leitura e percorro suas linhas usando o módulo csv.reader.
Filtrei os filmes do gênero "Adventure" e armazeno em uma lista chamada movies. No “if movie[‘id’]” verificamos que apenas um filme com o mesmo ID seja adicionado à lista “movies”, evitando filmes duplicados. Ordeno a lista de filmes pelo número de votos em ordem crescente.
Divido a lista de filmes em grupos de 100 filmes cada no “group”, defino uma função chamada get_movie_details que faz uma solicitação à API do TMDB para obter detalhes adicionais de um filme com base ID escolhido.
Para cada grupo de filmes, chamamos a função get_movie_details para obter os detalhes de cada filme e adiciona os detalhes ao dicionário do filme. Após isso, salvamos cada grupo de filmes em um arquivo JSON separado no diretório temporário.  Carrego os arquivos JSON do diretório temporário para o S3, usando o caminho de destino que inclui a data atual. Por fim, a função retorna um dicionário com o código de status 200 e a mensagem "Data ingestion complete".
Após a criação do código, vou ao AWS Lambda para executar:
![Lambda](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa2/printLambda/Capturar.PNG)
Execução do resultado:
![Resultado](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa2/printLambda/feito.PNG)
Quando executo o código, com a ajuda das credenciais e localização do bucket, os arquivos json vão ao bucket escolhido:
![bucket](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa2/printLambda/bucket.PNG)
* Tarefa 3

Questão 1: Importamos random. Cria-se uma variável que contém a função random.sample que retorna uma lista de amostras aleatórios de números de 1 a 250. A sequência é feita por range (1,251). Essa função retorna uma lista de 250 elementos aleatórios não repetidos. Por fim, colocamos o método reverse () na lista "listinha", após isso, imprimimos para obter o resultado.

Questão 2: Importamos o módulo csv e criamos uma lista com 20 nomes de animais. Usamos o método sort() para ordenar a lista em ordem crescente. Abrimos um arquivo chamado 'animais.csv' no modo de escrita ('w'). Criamos um objeto csv.writer para escrever no arquivo. Percorremos a lista de animais e escrevemos cada nome em uma nova linha do arquivo CSV usando o método writerow (). Após a conclusão do loop, o arquivo é fechado automaticamente. O código cria um arquivo CSV com os nomes dos animais em ordem crescente.

Questão 3: importamos names, random e time. A questão nos passa a definição da semente de aleatoriedade e o gerador de nomes aleatórios. Após isso, abriremos um arquivo chamado "nomes_aleatórios.txt" no modo de escrita ("w"). Dentro do with, usamos o for loop para cruzar cada nomes da lista "dados", a cada repetição escrevemos o nome do arquivo usando o método write () do objeto "arquivo". O "\n" serve para colocar o nome em cada nova linha. No final, imprimimos uma mensagem "pronto" como conclusão.

* Tarefa 4

Questão 1: Primeiro, usei o site Google Colaboratory para responder as questões. Baixei o pyspark e usei a importação Sparksession, alojei a variável "spark" de acordo com o que a questão passou, localizei onde o arquivo está acomodado e usei o comando que visualiza a tabela: df_nomes.show(5)
![um](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/um.PNG)

Questão 2: importei sparksession e define uma variável para ler o arquivo nomes_aleatorios.txt, logo depois, definir outra variável que substitui o nome da coluna anterior por outra, a coluna Nomes. Imprimi o esquema e exibi a coluna renomeada.
![dois](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/dois.PNG)

Questão 3: defino uma variável parar criar uma coluna com três valores alheatórios, usando a função rand () que gera número aleatório entre 0 e 1 para cada linha. A condição rand () < 1/3 significa que a probabilidade de ser "Fundamental" é de 1/3. A condição rand () < 2/3 significa que a probabilidade de ser "Médio" é de 1/3 (pois já descartamos a probabilidade de ser "Fundamental"). E a condição otherwise("Superior") significa que, se não atender a nenhuma das condições anteriores, o valor será "Superior"
![tres](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/tres.PNG)

Questão 4: Seguindo a mesma lógica da questão anterior, defini a variável para criar coluna, País, com 13 valores.
![quatro](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/quatro.PNG)

Questão 5: como os valores são extensos e daria trabalho escrever um por um os valores, usamos a função expr (), ele gera um número aleatório dentro de um intervalo que definimos. usando o rand () para multiplicar com os valores que queremos adicionamos o valor mínimo ("+1945") para ter o valor desejado. O floor () é para arredondar o resultado para que seja inteiro.
![cinco](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/cinco.PNG)

Questão 6: usando o filtro .where() para selecionar e pegar as linhas desejadas.
![seis](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/seis.PNG)

Questão 7: usamos novamente o filtro da questão anterior, mas dentro do comando spark.sql
![sete](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/sete.PNG)

Questão 8: criamos uma variável chamada df_millenials que armazena um dataframe filtrado contendo apenas as pessoas que nasceram entre 1980 e 1994. Em seguida, utilizamos o método count () para obter o número de linhas desse dataframe filtrado, representando a quantidade total de pessoas que pertencem a esse grupo.
![oito](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/oito.PNG)

Questão 9: repetimos a etapa anterior, mas com consulta SQL. Selecionamos todas as colunas dentro da tabela temporária "pessoas" que filtra o campo ano de nascimento entre 1980 e 1994. No final, usamos count () para obter a quantidade total de pessoas do filtro na consulta realizada.
![nove](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/nono.PNG)

Questão 10: usamos CASE WHEN para condicionar os anos solicitados pela questão e usando between para definir os intervalos de anos, denominamos de Geração. após isso, contabilizamos a quantidade de pessoas que pertencem a cada geração e país com COUNT (*). Por fim, fazemos a ordenação crescente de acordo com o solicitado com ORDER BY e agrupamos os dados por país e geração com GROUP BY.
![dez](https://github.com/Niwi01/AWS8/blob/master/Tarefas/Tarefa4/prints_reposta/dez.PNG)
### Aprendizado
* Tarefa 1

Ao observar e adicionar a chave de API que adicionei no código, compreendi como usar as APIs externas e validar as solicitações por causa da chave. Por último, ao fazer também, solicitações HTTP usando "requests", processando os dados em JSON dentro da variável "data" e usar o Pandas para criar um dataframe para organizar os dados de forma tabular.

* Tarefa 2

Aprendi como configurar o cliente s3 e usar suas funções para fazer o download de um arquivo do s3 para o diretório temporário e fazer upload de arquivos para o S3. Ler o arquivo csv e iterar sobre as linhas para extrair as informações desejadas.

Entendi a fazer chamadas para a API do TMDB usando a biblioteca requests para obter detalhes adicionais dos filmes com base em seus IDs do IMDb. E filtrar os filmes com base no gênero, classificar a lista de filmes por número de votos e dividir a lista em grupos menores. Também, criar arquivos JSON e salvá-los localmente no diretório temporário. E aprendi a configurar as credenciais de acesso do AWS S3 e a região correta para se comunicar com o serviço S3. Por fim, aprendi a usar o serviço Lambda da AWS para executar a função de ingestão de dados.

Por fim, entendi que tenho que criar uma função no AWS lambda com uma camada dentro com as importações de python para que eu consiga rodar o código dentro da função. E adquiri conhecimento sobre obter permissões, através da IAM, para ter acesso ao envio e upload de arquivos no Amazon S3.


* Tarefa 3

1 - Compreendi como utilizar a função random.sample (). Essa função retorna uma amostra aleatória de uma sequência. Usando os parâmetros adequados, especificando o intervalo desejado e quantidade de elementos a serem retornados. Obtendo, assim, uma lista de elementos aleatórios não repetidos.

2 - Usando o método "sort ()", ordeno de forma crescente a lista. Depois, abre-se um arquivo "animais.csv" e uso o objeto "csv.writer" para escrever cada nome de animal em uma nova linha do arquivo, no fim, é criado um arquivo csv contendo os nomes dos animais em ordem crescente.

3 - Compreendi que é possível abrir o arquivo "nomes_aleatórios.txt". Usando o for loop e escrever cada nome aleatório de lista "dados" no arquivo, com cada nome em uma nova linha. Por fim, o arquivo foi fechado automaticamente e há impressão "pronto".


* Tarefa 4

1 - Aprendi a utilizar a execução de códigos em PySpark, usando Google Colaboratory. Compreendi a importação da biblioteca SparkSession e a criação da variável spark para interagir com o ambiente Spark e, por fim, usar uma variável para ler o arquivo e listar as linhas através do show ().

2 -Aprendi ler o arquivo novamente e colocar dentro da variável que definimos na outra variável com o método withColumnRenamed() para renomear a única coluna existente. E visualizei o resultado com o método printSchema.

3 - Aprendi a criar uma nova coluna com condições utilizando a função withColumn e a função when. A usar a função rand () para gerar números aleatórios e como usar a função otherwise para definir um valor padrão quando as condições não forem atendidas.

4 - Aprendi a criar uma nova coluna com valores aleatórios usando a função withColumn e a função rand(). Entendi como definir a probabilidade de ocorrência de cada valor com base em intervalos.

5 - Aprendi a gerar valores aleatórios usando a função expr() e a função rand(). Compreendi como definir um intervalo de valores e adicionar um valor mínimo desejado utilizando a função floor ().

6 - Aprendi a filtrar linhas usando o método where() para selecionar e obter as linhas desejadas com base em uma condição.

7 - Aprendi a utilizar o Spark SQL para realizar consultas SQL. Compreendi como executar consultas com a função spark.sql() e realizar filtragens com base em condições.

8 - Que nem a questão 6, uso o método where(). Utilizei o método count () para obter o número total de linhas filtradas.

9 - Aprendi a realizar consultas SQL utilizando o Spark SQL com base em uma tabela temporária. Uso a função createOrReplaceTempView() para registrar uma tabela temporária e realizar consultas SQL utilizando a função spark.sql().

10 - Aprendi a usar a cláusula CASE WHEN em consultas SQL para realizar condições com base em intervalos de anos usando a cláusula BETWEEN. Compreendi como realizar a contagem de registros agrupados por país e geração utilizando a função count() e as cláusulas GROUP BY e ORDER BY em consultas SQL.
