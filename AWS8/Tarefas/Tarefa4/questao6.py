from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

df_select = df_nomes.where("AnoNascimento >= 2001")
df_select.show(10)