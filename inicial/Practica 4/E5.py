def calculo(numero):
    cumple = []
    for i in range(numero):
        cumple.append(i + 1)
    cumple_invertido = cumple[::-1]
    return cumple, cumple_invertido


edad = int(input("Ingrese su edad: "))

print(calculo(edad))
