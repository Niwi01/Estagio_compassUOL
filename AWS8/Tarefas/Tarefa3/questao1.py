#[Warm up]  Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. 
# Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

import random
#a funçao random.sample  pega uma sequencia, neste caso, lista. O valor 250 indica a quantidade de itens retornados.
listinha = random.sample(range(1,251),250)

#vemos o resultado padrão
print(listinha,'\n')
#invertemos
listinha.reverse()
print(listinha)
