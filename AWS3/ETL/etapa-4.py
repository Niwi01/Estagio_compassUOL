with open("actors.csv") as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')
    with open('etapa-4.txt', 'w') as txt:

        freq = {}
        maxi=0
        for a in dados[1:]:
            campo1 = a.strip().split(',')[4]

            if campo1 not in freq:
                freq[campo1] = 1
            else:
                freq[campo1] += 1


        filme = max(freq, key=freq.get)
        numero = freq[filme]

        txt.write(f'{filme}: {numero}')
