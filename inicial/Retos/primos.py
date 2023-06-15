"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""


def es_primo(numero):
    contador = 0

    for i in range(2, numero):
        if numero % i == 0:
            contador += 1

    if contador == 0:
        print("El numero %s es primo" % numero)
    else:
        print("El numero %s no es primo" % numero)


es_primo(int(input("ingresar num")))

for i in range(100):
    es_primo(i)
