from tkinter import *

principal = Tk()

principal.geometry("595x700")  # tamaño de ventana

# declaración de todas las variables asociadas a los entrys del programa:
var_id = StringVar()
var_cobre = IntVar()
var_aceite = IntVar()
var_pintura = IntVar()
var_ogp = IntVar()
var_mo = IntVar()
var_id_buscar = StringVar()
var_id_borrar = StringVar()
var_ordenar = StringVar()

# declaracion de los entry para que el usuario cargue datos:
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

id_buscar = Entry(principal, textvariable=var_id_buscar, width=14)
id_buscar.grid(row=1, column=7)

id_borrar = Entry(principal, textvariable=var_id_borrar, width=14)
id_borrar.grid(row=3, column=7)

ordenar = Entry(principal, textvariable=var_ordenar, width=14)
ordenar.grid(row=5, column=7)

# declaración de los labels que le indican al usuario que datos ingresar:
label_id = Label(principal, text="ID del Transformador: ")
label_id.grid(row=1, column=0, sticky=W)

label_cobre = Label(principal, text="Kg de cobre: ")
label_cobre.grid(row=2, column=0, sticky=W)

label_aceite = Label(principal, text="Litros de Aceite:")
label_aceite.grid(row=3, column=0, sticky=W)

label_pintura = Label(principal, text="Litros de Pintura:")
label_pintura.grid(row=4, column=0, sticky=W)

label_ogp = Label(principal, text="OGP: ")
label_ogp.grid(row=1, column=2, sticky=W)

label_mo = Label(principal, text="Mano de obra:")
label_mo.grid(row=2, column=2, sticky=W)

label_costo_fijo = Label(principal, text="Costo fijo promedio:")
label_costo_fijo.grid(row=3, column=2, sticky=W)

lavel_valor_costo_fijo = Label(
    principal, text="600.000", borderwidth=3, relief="groove", width=12
)
lavel_valor_costo_fijo.grid(row=3, column=3, sticky=W)

# declaracion de las function que van a ser llamadas por los botones:


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


# definición de los notones de alta, modficar, buscar y ordenar:

alta = Button(principal, text="alta", command=alta, width=10, background="lightgreen")
alta.grid(row=5, column=1, pady=3)

modificar = Button(
    principal, text="modificar", command=modificar, width=10, background="lightblue"
)
modificar.grid(row=5, column=2)

buscar_id = Button(
    principal, text="Buscar ID", command=buscar_id, width=10, background="yellow"
)
buscar_id.grid(row=1, column=5, padx=3, pady=3)

borrar_id = Button(
    principal, text="Borrar ID", command=borrar_id, background="red", width=10
)
borrar_id.grid(row=3, column=5, padx=3, pady=1)

ordenar = Button(principal, text="Ordenar por:", command=ordenar, width=10)
ordenar.grid(row=5, column=5)

mainloop()  # loop de la interfaz
