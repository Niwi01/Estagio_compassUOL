def my_map(list, f):
    lista = []
    for e in list:
        funcao = f(e)
        lista.append(funcao)
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = my_map(lista, lambda x: x**2)
print(lista2)
    