#Apresente a média da coluna contendo o número de filmes.
import pandas as pd

media = pd.read_csv("actors.csv", encoding='utf-8')

calculo = media['Number of Movies'].mean()

print(f'A média do número de filmes é {calculo}')
