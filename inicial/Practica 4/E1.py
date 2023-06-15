es_par = lambda numero: numero % 2

numero = int(input("Ingrese un numero"))

if es_par(numero) == 0:
    print("Es par")
else:
    print("Es impar")
