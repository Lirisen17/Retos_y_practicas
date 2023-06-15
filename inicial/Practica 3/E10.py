password = "asdasd"
n = "a"

while n != password:
    n = str(input("Ingrese la contraseña: "))
    if n == password:
        print("Contraseña correcta!")
    else:
        print("Te equivocaste, volve a intentar!")
