import sys

numeros = []

for i in range(1, 4):
    numeros.append(int(sys.argv[i]))
    if numeros[i - 1] % 2 == 0:
        print("el numero %s es par" % numeros[i - 1])
    else:
        print("el numero %s es impar" % numeros[i - 1])
