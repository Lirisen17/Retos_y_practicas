a = 0
b = []
n = True
compra_total = []
precio_total = 0
lista_1 = []
j = True

while j:
    while n:
        item = {
            "producto": input("Ingrese el nombre del producto:"),
            "precio": int(input("Ingrese el precio del producto: ")),
            "cantidad": int(input("ingrese la cantidad en kilos del producto: ")),
        }  # Guardo en un diccionario los valores actuales
        compra_total.append(item)  # guardo en una lista para no pisarlo
        precio_item = item["precio"] * item["cantidad"]
        precio_total = (
            precio_total + precio_item
        )  # acumulo el precio total de la compra
        seguir = int(input("Si desea agregar otro item presione 1 sino pulse 0"))
        if seguir != 1:
            print("Compra Registrada!")
            lista_1.append(compra_total)
            break
    seguir_2 = int(input("Si desea agregar otra compra presione 1 sino pulse 0"))
    if seguir_2 != 1:
        break

print("La lista total de compras es \n", lista_1)
