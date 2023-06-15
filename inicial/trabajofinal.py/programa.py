from tkinter import *

principal = Tk()

principal.geometry("1000x700")

var_id = StringVar()
var_cobre = IntVar()
var_aceite = IntVar()
var_pintura = IntVar()
var_ogp = IntVar()
var_mo = IntVar()
var_id_buscar = StringVar()
var_id_borrar = StringVar()

Label(principal, text="ID del Transformador: ").grid(row=1, column=0, sticky=W)
Label(principal, text="Kg de cobre: ").grid(row=2, column=0, sticky=W)
Label(principal, text="Litros de Aceite:").grid(row=3, column=0, sticky=W)
Label(principal, text="Litros de Pintura:").grid(row=4, column=0, sticky=W)
Label(principal, text="OGP: ").grid(row=1, column=2, sticky=W)
Label(principal, text="Mano de obra:").grid(row=2, column=2, sticky=W)
Label(principal, text="Costo fijo promedio:").grid(row=3, column=2, sticky=W)
Label(principal, text="600.000").grid(row=3, column=3, sticky=W)

id_transformador = Entry(principal, textvariable=var_id, width=14)
id_transformador.grid(row=1, column=1)
cobre = Entry(principal, textvariable=var_cobre, width=14)
cobre.grid(row=2, column=1)
aceite = Entry(principal, textvariable=var_aceite, width=14)
aceite.grid(row=3, column=1)
pintura = Entry(principal, textvariable=var_pintura, width=14)
pintura.grid(row=4, column=1)
ogp = Entry(principal, textvariable=var_ogp, width=14)
ogp.grid(row=1, column=3)
mo = Entry(principal, textvariable=var_mo, width=14)
mo.grid(row=2, column=3)


def alta():
    pass


def modificar():
    pass


def buscar_id():
    pass


def borrar_id():
    pass


def ordenar():
    pass


alta = Button(principal, text="alta", command=alta).grid(row=5, column=1)
modificar = Button(principal, text="modificar", command=modificar).grid(row=5, column=2)


buscar_id = Button(principal, text="Buscar por ID", command=buscar_id).grid(
    row=1, column=5
)

id_buscar = Entry(principal, textvariable=var_id_buscar, width=14)
id_buscar.grid(row=1, column=6)

borrar_id = Button(principal, text="Borrar por ID", command=borrar_id).grid(
    row=3, column=5
)

id_borrar = Entry(principal, textvariable=var_id_borrar, width=14)
id_borrar.grid(row=3, column=6)

ordenar = Button(principal, text="Ordenar por:", command=ordenar).grid(row=5, column=5)

mainloop()
