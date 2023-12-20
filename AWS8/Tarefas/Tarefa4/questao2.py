from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

df_nomes = spark.read.csv("/content/nomes_aleatorios.txt")
df_nomes = df_nomes.withColumnRenamed("_c0","Nomes")
df_nomes['Nomes']
df_nomes.printSchema()
df_nomes.show(10)