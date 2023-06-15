import sys

numero_1 = int(sys.argv[1])
numero_2 = int(sys.argv[2])
numero_3 = int(sys.argv[3])

if (numero_1 % 2) == 0:
    print("El numero", numero_1, "es par")
else:
    print("El numero", numero_1, "es impar")

if (numero_2 % 2) == 0:
    print("El numero", numero_2, "es par")
else:
    print("El numero", numero_2, "es impar")

if (numero_3 % 2) == 0:
    print("El numero", numero_3, "es par")
else:
    print("El numero", numero_3, "es impar")
