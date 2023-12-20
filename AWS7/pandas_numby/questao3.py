#Apresente o nome do ator/atriz com a maior média por filme.
import pandas as pd

ator = pd.read_csv("actors.csv", encoding='utf-8')

grupo = ator.groupby('Actor')['Average per Movie'].sum()
grupo2 = grupo.sort_values(ascending=False)

print(f'O ator {grupo2.index[0]} tem a maior média por filme: {grupo2.iloc[0]}')

