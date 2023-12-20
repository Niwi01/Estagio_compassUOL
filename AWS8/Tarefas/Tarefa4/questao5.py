from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import floor, expr

df_nomes = df_nomes.withColumn("AnoNascimento", floor(expr("rand() * (2010 - 1945 + 1) + 1945")))
df_nomes.show(20)