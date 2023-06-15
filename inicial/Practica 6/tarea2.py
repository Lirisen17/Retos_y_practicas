""" TAREA 2

A partir del ejercicio desafío de la unidad anterior cree una
aplicación que permita realizar un alta de registros en la base de datos (sqlite3) """

from tkinter import *
import sqlite3

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


def crear_conexion():
    con = sqlite3.connect("base_tarea_2.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS titulos(titulo text, ruta text, descripcion text)"
    cursor.execute(sql)
    con.commit()


def alta():
    global conexion
    cursor = conexion.cursor()
    data = (var_titulo.get(), var_ruta.get(), var_descripcion.get())
    sql = "INSERT INTO titulos(titulo, ruta, descripcion) VALUES(?,?,?)"
    cursor.execute(sql, data)
    conexion.commit()


def sorpresa():
    ventana.configure(bg="red")


def print_db():
    global conexion
    cursor = conexion.cursor()
    sql = "SELECT * FROM titulos"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)


conexion = crear_conexion()
crear_tabla(conexion)

boton_alta = Button(ventana, text="alta", command=alta, width=10)
boton_alta.grid(row=4, column=0, pady=3)
boton_sorpresa = Button(ventana, text="sorpresa", command=sorpresa, width=10)
boton_sorpresa.grid(row=4, column=1)
boton_mostrar = Button(ventana, text="print", command=print_db, width=10)
boton_mostrar.grid(row=4, column=2)

mainloop()
