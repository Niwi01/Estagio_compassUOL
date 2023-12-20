from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when

df_nomes = spark.read.csv("/content/nomes_aleatorios.txt")
df_nomes = df_nomes.withColumnRenamed("_c0","Nomes")
df_nomes = df_nomes.withColumn("Escolaridade", when(rand()<1/3,"Fundamental").
                         when(rand()<2/3,"Medio").
                         otherwise("Superior"))

df_nomes.show(10)