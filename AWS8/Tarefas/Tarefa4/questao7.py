from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

df_nomes = spark.read.csv("/content/nomes_aleatorios.txt")

from pyspark.sql.functions import rand, when

df_nomes = df_nomes.withColumn("Escolaridade", when(rand()<1/3,"Fundamental").
                         when(rand()<2/3,"Medio").
                         otherwise("Superior"))

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("select * from pessoas where AnoNascimento >= 2001").show()
