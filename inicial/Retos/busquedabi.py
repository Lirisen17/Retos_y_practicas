# busqueda binaria

lista = []
inicio = 0


for i in range(100):
    lista.append(i)

final = len(lista) - 1
buscar = int(input("Ingresar valor a buscar"))


def busqueda(lista, inicio, final, buscar):
    if inicio > final:
        return False
    centro = (inicio + final) // 2
    if lista[centro] == buscar:
        print(centro)
    elif lista[centro] < buscar:
        busqueda(lista, centro + 1, final, buscar)
    else:
        busqueda(lista, inicio, centro - 1, buscar)


busqueda(lista, inicio, final, buscar)
