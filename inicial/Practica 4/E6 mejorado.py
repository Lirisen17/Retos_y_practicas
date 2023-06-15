lista_ordenada = []
lista1 = [3, 44, 21, 78, 5, 56, 9]


def ordenar():
    global lista1, lista_ordenada
    posicion = 0
    if lista1:
        numero_menor = lista1[0]
        for i in lista1:
            if numero_menor > i:
                posicion = lista1.index(i)
                numero_menor = i
        lista_ordenada.append(numero_menor)
        lista1.pop(posicion)
        ordenar()
    return lista_ordenada


print(ordenar())
