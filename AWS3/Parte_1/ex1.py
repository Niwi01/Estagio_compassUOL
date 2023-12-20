from datetime import datetime

nome = str(input('Seu nome: '))
idade_atual = int(input('Idade: '))
ano_atual = datetime.now().year
nascimento = (ano_atual)-(idade_atual)

futuro = nascimento + 100

print(futuro)