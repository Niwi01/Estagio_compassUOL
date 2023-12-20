with open("actors.csv") as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')
    with open('etapa-2.txt', 'w') as txt:
        for x in dados[1:]:
            campo1 = x.strip().split(',')[3]
            campo2 = x.strip().split(',')[0]

            txt.write(f'{campo2}: {campo1}\n')