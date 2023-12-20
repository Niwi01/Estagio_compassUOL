from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when

df_nomes = spark.read.csv("/content/nomes_aleatorios.txt")
df_nomes = df_nomes.withColumnRenamed("_c0","Nomes")
df_nomes = df_nomes.withColumn("Pais",
                         when(rand()<1/13,"Brasil").
                         when(rand()<2/13,"Afeganistao").
                         when(rand()<3/13,"Belgica").
                         when(rand()<4/13,"Canadá").
                         when(rand()<5/13,"China").
                         when(rand()<6/13,"Vaticano").
                         when(rand()<7/13,"Uruguai").
                         when(rand()<8/13,"Tailandia").
                         when(rand()<9/13,"Sudao").
                         when(rand()<10/13,"Russia").
                         when(rand()<11/13,"Nepal").
                         when(rand()<12/13,"Peru").
                         otherwise("Madagascar"))
df_nomes.show(10)