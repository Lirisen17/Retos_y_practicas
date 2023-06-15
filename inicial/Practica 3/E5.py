a = 0
b = []
n = True
compra_total = []
precio_total = 0

while n:
    item = {
        "producto": input("Ingrese el nombre del producto:"),
        "precio": int(input("Ingrese el precio del producto: ")),
        "cantidad": int(input("ingrese la cantidad en kilos del producto: ")),
    }  # Guardo en un diccionario los valores actuales
    compra_total.append(item)  # guardo en una lista para no pisarlo
    precio_item = item["precio"] * item["cantidad"]
    precio_total = precio_total + precio_item  # acumulo el precio total de la compra
    seguir = int(input("Si desea agregar otro elemento presione 1 sino pulse 0"))
    if seguir != 1:

        break


print("El precio total de su compra es", precio_total)
print("el detalle de su compra es: \n", compra_total)
