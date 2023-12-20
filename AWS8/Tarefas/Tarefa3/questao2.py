#Em Python, declare e inicialize uma lista contendo o nome de 20 animais. 
#Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui).  
#Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.

import csv
animalzinhos = ["gato", "girafa", "cachorro", "abelha", "calopsita", "camarao", "camaleao", "camelo", "canario", "gavial", "gaviao", "lagartixa", "lagosta", "mamute",
                "pato", "pavao", "vaca", "urso-panda", "passaro", "zebra"]

#a lista terá ordem crescente
animalzinhos.sort()

with open('animal.csv','w', newline='') as arquivo:
    listinha = csv.writer(arquivo)
    for animais in animalzinhos:
        listinha.writerow([animais])
print("prontinho")

