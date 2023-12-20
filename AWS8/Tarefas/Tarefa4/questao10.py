from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
spark = SparkSession.builder.master("local[*]").appName("Exercicio").getOrCreate()

df_nomes.createOrReplaceTempView("pessoas")
df_quantidade = spark.sql("""SELECT Pais, 
                          CASE 
                          WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers' 
                          WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X' 
                          WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials' 
                          WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z' 
                          ELSE 'Outra Geracao' 
                          END as Geracao, 
                          COUNT(*) as Quantidade_pessoas 
                          FROM pessoas 
                          GROUP BY Pais, Geracao
                          ORDER BY Pais, Geracao, COUNT(*)""")

df_quantidade.show()