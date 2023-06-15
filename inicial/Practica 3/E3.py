frase = input("por favor inserte una frase ")
contador = 0

for i in frase:
    if (
        i == "á"
        or i == "Á"
        or i == "é"
        or i == "É"
        or i == "í"
        or i == "Í"
        or i == "ó"
        or i == "Ó"
        or i == "ú"
        or i == "Ú"
    ):
        contador += 1


print("La cantidad de letras con tilde en la frase ingresada es %s" % contador)
