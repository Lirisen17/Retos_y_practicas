c = True
lista_compras = []  # defino la lista de compras totales
compra_nueva = []  # defino la lista de compra actual
seguir = 1
pregunta = 1


def Alta(s, compra_nueva):
    while s == 1:
        item = [
            input("Ingrese el nombre del producto:"),
            int(input("Ingrese el precio del producto: ")),
            int(input("ingrese la cantidad en kilos del producto: ")),
        ]  # Guardo en una lista los valores actuales
        compra_nueva.append(item)  # guardo en una lista para no pisarlo
        s = int(input("Si desea agregar otro item presione 1 sino pulse 0"))
        if s == 0:
            return compra_nueva


def Baja(indice, lista_compras):
    lista_compras.pop(indice)
    return lista_compras


def Consulta(lista_compras):
    print(lista_compras)


def Modificar(index, lista_compras, index_2):
    item_modificado = [
        input("Ingrese el nombre del producto:"),
        int(input("Ingrese el precio del producto: ")),
        int(input("ingrese la cantidad en kilos del producto: ")),
    ]  # Guardo en una lista los valores actuales
    lista_compras[index][index_2] = item_modificado
    item_modificado = []

    print("Item Modificado!")


while c:
    opcion = input("Alta-Baja-Consulta-Modificar-Salir ")
    if opcion == "Alta":
        Alta(seguir, compra_nueva)
        lista_compras.append(compra_nueva)
        compra_nueva = []
    elif opcion == "Baja":
        indice = int(input("Ingresar el numero de compra que desea borrar"))
        lista_compras = Baja(indice, lista_compras)
    elif opcion == "Consulta":
        Consulta(lista_compras)
    elif opcion == "Modificar":
        while pregunta == 1:
            index = int(input("Ingresar el numero de la compra que quiere modificar"))
            index_2 = int(
                input("Que num de item quiere modificar de la compra %s ?" % index)
            )
            Modificar(index, lista_compras, index_2)
            pregunta = int(input("seguir modificando la compra indicada? 1 si, 0 no "))
            if pregunta == 0:
                break
    else:
        break

