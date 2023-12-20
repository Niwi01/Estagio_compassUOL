with open("actors.csv") as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')
    with open('etapa-3.txt', 'w') as txt:
        x = float(0)
        num = []
        actors = []
        c = 0

        for valores in dados[1:]:
            campo1 = valores.strip().split(',')[3]
            campo2 = valores.strip().split(',')[0]
            num.append(float(campo1))
            actors.append(campo2)

        for valor in num:
            if valor >= x:
                x = valor
                actor=actors[c]
            c += 1
        txt.write(f'{actor} tem a maior media de faturamento:{x}')
