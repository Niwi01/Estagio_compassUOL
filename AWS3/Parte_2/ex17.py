lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def numeros(lista):
    lis = int(len(lista)/3)
    lis2 = lis * 2
    lista1 = lista[:lis]
    lista2= lista[lis:lis2]
    lista3 = lista[lis2:]
    print(lista1, lista2, lista3)
    
numeros(lista)