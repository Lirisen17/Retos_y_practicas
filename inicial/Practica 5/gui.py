from tkinter import *

ventana = Tk()

var_titulo = StringVar()
var_ruta = StringVar()
var_descripcion = StringVar()

titulo = Label(
    ventana,
    text="Ingrese sus datos",
    bg="DarkOrchid3",
    fg="thistle1",
    height=1,
    width=40,
)
titulo.grid(row=0, column=0, columnspan=4)
Label(ventana, text="Titulo").grid(row=1, column=0, sticky=W)
Label(ventana, text="Ruta").grid(row=2, column=0, sticky=W)
Label(ventana, text="Descripción").grid(row=3, column=0, sticky=W)

titulo = Entry(ventana, textvariable=var_titulo)
titulo.grid(row=1, column=1)
ruta = Entry(ventana, textvariable=var_ruta)
ruta.grid(row=2, column=1)
descripcion = Entry(ventana, textvariable=var_descripcion)
descripcion.grid(row=3, column=1)


def print_consola():
    print("Nueva alta de datos!")
    print("{0} {1} {2}".format(var_titulo.get(), var_ruta.get(), var_descripcion.get()))


def sorpresa():
    ventana.configure(bg="red")


alta = Button(ventana, text="alta", command=print_consola).grid(row=4, column=0)
sorpresa = Button(ventana, text="sorpresa", command=sorpresa).grid(row=4, column=1)

mainloop()
