PI = 3.1415
radio = float(input("Ingrese el radio de la circunferencia: "))


def perimetro_circunferencia(radio, PI):

    return 2 * PI * radio


print("El perimetro es ", perimetro_circunferencia(radio, PI))


def area_circunferencia(radio, PI):

    return PI * radio**2


print("El area es ", area_circunferencia(radio, PI))

numero = int(input("ingrese un numero entero para incrementarlo en el 10% "))


def incremento_10(numero):
    return numero * 1.1


print(incremento_10(numero))
