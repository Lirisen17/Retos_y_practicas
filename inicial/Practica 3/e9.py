corte_while = 1
compra_nueva = {}
item = {}
diccionario_compras = {}
f = 0
posicion = 0
compra_modificada = {}


def Alta(cantidad_items):

    for posicion in range(cantidad_items):
        item = {
            "Nombre": input("nombre del producto: "),
            "Cantidad": input("cantidad: "),
            "Precio": input("precio"),
        }
        compra_nueva[posicion] = item
        item = {}


def Consulta():
    print(diccionario_compras.values())


def Modificar(cantidad_items):
    for posicion in range(cantidad_items):
        item = {
            "Nombre": input("nombre del producto: "),
            "Cantidad": input("cantidad: "),
            "Precio": input("precio"),
        }
        compra_modificada[posicion] = item
        item = {}


def Baja(eliminar_compra):
    del diccionario_compras[eliminar_compra]


while corte_while == 1:
    input_usuario = int(input("1:Alta, 2:Consulta, 3:Modificar, 4:Baja, 5: Salir "))
    if input_usuario == 1:
        cantidad_items = int(input("Cuantos items tiene la compra que desea realizar?"))
        Alta(cantidad_items)
        diccionario_compras[f] = compra_nueva
        f += 1
        compra_nueva = {}
        print("Compra registrada!")
    elif input_usuario == 2:
        Consulta()
    elif input_usuario == 3:
        mod = int(input("Que compra quiere modificar?"))
        cantidad_items = int(input("Cuantos items tiene la compra que desea realizar?"))
        Modificar(cantidad_items)
        diccionario_compras[mod] = compra_modificada
        compra_modificada = {}
    elif input_usuario == 4:
        eliminar_compra = int(input("Que compra desea borrar?"))
        Baja(eliminar_compra)
    elif input_usuario == 5:
        print("Programa finalizado!")
        corte_while = 0
    else:
        print("Opcion invalida!")
