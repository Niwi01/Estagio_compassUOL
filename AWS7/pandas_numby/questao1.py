#Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
import pandas as pd

ator = pd.read_csv("actors.csv", encoding='utf-8')


grupo = ator.groupby('Actor')['Number of Movies'].sum()
grupo2 = grupo.sort_values(ascending=False)

print(f'O ator/atriz com maior número de filmes é {grupo2.index[0]} com {grupo2.iloc[0]} filmes')


