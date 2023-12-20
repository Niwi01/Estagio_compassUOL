import random
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)
random_list.sort()

media = sum(random_list)/len(random_list)

n = len(random_list)
if n%2 == 0:
    med1 = random_list[n//2]
    med2 = random_list[n//2-1]
    mediana = (med1+med2)/2
else:
    mediana = random_list[n//2]


valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')