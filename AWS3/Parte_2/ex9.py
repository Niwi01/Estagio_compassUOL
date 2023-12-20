primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

list1 = []

for nu, (n, s, i) in enumerate(zip(primeirosNomes,sobreNomes,idades)):
    frase = f'{nu} - '+ " ".join([n, s, 'está com', str(i),'anos'])
    list1.append(frase)

for frase in list1:
    print(frase)