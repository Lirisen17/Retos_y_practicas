# 1) Crear una app que realice un alta de registros de los siguientes campos:
# producto
# descripción
# 2) La app debe estar realizada con tkinter y sqlite3
# 3) El campo "producto" debe de contener solo caracteres alfanuméricos.
# 4) La información debe poder presentarse en pantalla mediante un treeview

from tkinter import (
    Tk,
    IntVar,
    StringVar,
    CENTER,
    Label,
    Button,
    Entry,
    mainloop,
    messagebox,
)
from tkinter import ttk
import sqlite3
import re

root = Tk()
producto = StringVar()
descripcion = StringVar()


def conexion_sqlite():
    con = sqlite3.connect("base_stock.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS stock(id integer PRIMARY KEY autoincrement,producto string,descripcion string)"
    cursor.execute(sql)
    con.commit()


def mostrar(con):
    cursor = con.cursor()
    sql = "SELECT * FROM stock"
    cursor.execute(sql)
    res = cursor.fetchall()
    tree.delete(*tree.get_children())
    for i in res:
        tree.insert(
            "",
            "end",
            text=i[0],
            values=(
                i[1],
                i[2],
            ),
        )


def alta(con, producto, desc):
    patron = "^[A-Za-z0-9áéíóúÁÉÍÓÚ]*$"
    cadena = producto.get()
    if re.match(patron, cadena):
        cursor = con.cursor()
        data = (producto.get(), desc.get())
        sql = "INSERT into stock(producto,descripcion) VALUES(?,?)"
        cursor.execute(sql, data)
        conexion.commit()
        mostrar(con)
    else:
        messagebox.showinfo(
            message="El producto solo acepta caracteres alfanumericos.", title="Error"
        )


conexion = conexion_sqlite()
crear_tabla(conexion)

label_producto = Label(root, text="Producto: ")
label_producto.grid(column=0, row=0)
label_descripcion = Label(root, text="Descripcion: ")
label_descripcion.grid(column=0, row=1)

producto_entry = Entry(root, textvariable=producto)
producto_entry.grid(column=1, row=0)
descripcion_entry = Entry(root, textvariable=descripcion)
descripcion_entry.grid(column=1, row=1)

alta_boton = Button(
    root,
    text="Dar Alta",
    command=lambda: alta(conexion, producto, descripcion),
    width=35,
    background="orange",
)
alta_boton.grid(column=0, row=2, columnspan=3, pady=3)

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2")

tree.column("#0", width=90, anchor=CENTER)
tree.column("col1", width=90, anchor=CENTER)
tree.column("col2", width=90, anchor=CENTER)

tree.heading("#0", text="ID")
tree.heading("col1", text="Producto")
tree.heading("col2", text="Descrpicion")

tree.grid(column=0, row=3, columnspan=3)
mostrar(conexion)
mainloop()
