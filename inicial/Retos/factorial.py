"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */

"""


def factorial(n):
    if n > 1:
        resultado = n * factorial(n - 1)
    else:
        resultado = 1
    return resultado


print("El factorial es", factorial(int(input("Ingresar num: "))))
