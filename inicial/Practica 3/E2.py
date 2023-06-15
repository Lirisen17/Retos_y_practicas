frase = input("por favor inserte una frase ")
contador = 0

for i in frase:
    if i == "a":
        contador += 1


print("La cantidad de letras 'a' en la frase ingresada es %s" % contador)
