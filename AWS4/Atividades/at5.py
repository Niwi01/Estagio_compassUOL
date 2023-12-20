from csv import reader

with open("estudantes.csv") as arquivo:
    boletim = reader(arquivo)
    for l in sorted(boletim):
        aluno = l[0]
        notas = l[1:]
        nota_em_numero = list(map(int, notas))
        maiores_notas = sorted(nota_em_numero, reverse=True)[:3]
        media = round(sum(maiores_notas) / 3, 2)
        print(f"Nome: {aluno} Notas: {maiores_notas} Média: {media}")
