"""TAREA 3

A partir del ejercicio desafío de la unidad anterior 
cree una aplicación que permita realizar un alta de registros en un archivo de texto (.txt)"""


from tkinter import *

ventana = Tk()

var_titulo = StringVar()
var_ruta = StringVar()
var_descripcion = StringVar()
archivo = ""


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


def alta():
    archivo = open("tarea3.txt", "a")
    data = str(
        (var_titulo.get())
        + " "
        + str(var_ruta.get())
        + " "
        + str(var_descripcion.get())
    )
    archivo.write(str(data))
    archivo.write("\n")
    archivo.close
    return archivo


def sorpresa():
    ventana.configure(bg="red")


def print_text():
    global archivo
    archivo = open("tarea3.txt", "r")
    for i in archivo:
        print(i)
    archivo.close


boton_alta = Button(ventana, text="alta", command=alta, width=10)
boton_alta.grid(row=4, column=0, pady=3)
boton_sorpresa = Button(ventana, text="sorpresa", command=sorpresa, width=10)
boton_sorpresa.grid(row=4, column=1)
boton_mostrar = Button(ventana, text="print", command=print_text, width=10)
boton_mostrar.grid(row=4, column=2)


mainloop()
