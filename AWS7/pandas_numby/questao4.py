#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

ator = pd.read_csv("actors.csv", encoding='utf-8')

freq = ator['#1 Movie'].value_counts()

print(f'O filme {freq.index[0]} aparece {freq.iloc[0]} vez(es) no dataset')






