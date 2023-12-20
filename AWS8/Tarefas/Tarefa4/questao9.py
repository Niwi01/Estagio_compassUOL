
df_nomes.createOrReplaceTempView("pessoas")
df_sql = spark.sql("select * from pessoas where AnoNascimento >= 1980 and AnoNascimento <= 1994")
df_sql.count()