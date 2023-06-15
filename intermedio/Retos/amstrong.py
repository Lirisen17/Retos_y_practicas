# es igual a la suma de sus dígitos elevados a la potencia de su número de cifras


def amstrong(numero):
    sumas = 0
    digitos = len(str(numero))
    for i in str(numero):
        sumas += int(i) ** digitos

    if sumas == numero:
        return True


n = int(input("Ingrese el numero para saber si es de amstrong o no: "))
print(amstrong(n))
