
df_millenials = df_nomes.where("AnoNascimento >= 1980 and AnoNascimento <= 1994")
df_millenials.count()