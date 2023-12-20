lista = []

with open('actors.csv') as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')

    for linha in dados[1:]:
        ator = (linha.split(",")[0])
        valor = (linha.split(",")[1])
        lista.append({'ator':ator, 'valor':valor})

    lista = sorted(lista, key=lambda dicionario: dicionario["valor"], reverse=True)

    with open('etapa-5.txt', 'w') as txt:
        for dicionario in lista:
            txt.write(f'O ator {dicionario["ator"]} tem {dicionario["valor"]} de faturamento\n')
