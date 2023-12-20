with open("actors.csv") as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')
    with open('etapa-1.txt', 'w') as txt:
        quantidade = 0
        atores = []
        #quantidade
        for m in dados[1:]:
            campo1 = m.strip().split(',')[2]
            campo2 = m.strip().split(',')[0]
            maior = int(campo1)

            if maior > quantidade:
                quantidade=maior
                atores=campo2

        txt.write(f'O ator maior numero de filmes e {atores} com {quantidade} filmes.')

