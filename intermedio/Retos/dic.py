dic1 = {
    "persona": {"nombre": "Pedro", "apellido": "Gomez"},
    "edad": 23,
    "profesion": "pintor",
}
dic2 = {
    "persona": {"nombre": "Anna", "apellido": "Rodríguez"},
    "edad": 33,
    "profesion": "chef",
}
dic3 = {1: dic1, 2: dic2}
list3 = [dic1, dic2]


def recorrer_dic(dic3):
    for i in dic3:
        # print (dic3[i])
        for e in dic3[i]:
            print(dic3[i][e])
            for h in dic3[i][e]:
                print(h)


recorrer_dic(dic3)


def ejercicio4():
    lista1 = []
    for i in dic3:
        lista1.append(dic3[i]["persona"].values())
    print(lista1[0])


def ejercicio1():
    print(dic3.keys())


def ejercicio2():
    print(dic2.values())


def ejercicio3():
    print(dic3)


# ejercicio4()
