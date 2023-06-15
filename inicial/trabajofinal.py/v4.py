from tkinter import *
from tkinter import ttk
import sqlite3

principal = Tk()

principal.geometry("730x400")  # tamaño de ventana

# declaración de todas las variables asociadas a los entrys del programa:
var_num_de_transformador = IntVar()
var_cobre = IntVar()
var_aceite = IntVar()
var_pintura = IntVar()
var_ogp = IntVar()
var_mo = IntVar()
var_id_buscar = IntVar()
var_id_borrar = IntVar()
var_ordenar = StringVar()
costo_fijo = 400
valor_transformador = 3750
precio_cobre = 16
precio_pintura = 10
precio_aceite = 2
precio_mo = 2
margen = 0

# declaracion de los entry para que el usuario cargue datos:
numero_transformador = Entry(principal, textvariable=var_num_de_transformador, width=14)
numero_transformador.grid(row=1, column=1)

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
id_buscar.grid(row=1, column=6)

id_borrar = Entry(principal, textvariable=var_id_borrar, width=14)
id_borrar.grid(row=5, column=6)


# declaración de los labels que le indican al usuario que datos ingresar:
label_id = Label(principal, text="ID del Transformador: ")
label_id.grid(row=1, column=0, sticky=W)

label_cobre = Label(principal, text="Kg de cobre: ")
label_cobre.grid(row=2, column=0, sticky=W)

label_aceite = Label(principal, text="Lts de Aceite:")
label_aceite.grid(row=3, column=0, sticky=W)

label_pintura = Label(principal, text="Lts de Pintura:")
label_pintura.grid(row=4, column=0, sticky=W)

label_ogp = Label(principal, text="Precio de OGPs: ")
label_ogp.grid(row=1, column=2, sticky=W)

label_mo = Label(principal, text="Hs Mano de obra:")
label_mo.grid(row=2, column=2, sticky=W)

label_costo_fijo = Label(principal, text="Costo fijo promedio:")
label_costo_fijo.grid(row=3, column=2, sticky=W)

lavel_valor_costo_fijo = Label(
    principal, text=costo_fijo, borderwidth=3, relief="groove", width=12
)
lavel_valor_costo_fijo.grid(row=3, column=3, pady=3)

# crear base y tabla sqlite
def crear_conexion():
    con = sqlite3.connect("base_trafos.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS transformadores(id integer PRIMARY KEY NOT NULL, cobre integer,pintura integer, aceite integer, mo integer, ogp integer, costos_fijos integer,valor_transformador integer, margen integer)"
    cursor.execute(sql)
    con.commit()


conexion = crear_conexion()
crear_tabla(conexion)

# declaracion de las function que van a ser llamadas por los botones:


def alta_trafo():
    global var_aceite, var_cobre, var_num_de_transformador, var_mo, var_ogp, var_pintura, valor_transformador, costo_fijo, conexion, margen

    cursor = conexion.cursor()
    margen = (
        int(valor_transformador)
        - int(var_aceite.get() * precio_aceite)
        - int(var_cobre.get() * precio_cobre)
        - int(var_mo.get() * precio_mo)
        - int(var_pintura.get() * precio_pintura)
        - int(costo_fijo)
        - int(var_ogp.get())
    )
    data = (
        int(var_num_de_transformador.get()),
        int(var_cobre.get() * precio_cobre),
        int(var_pintura.get() * precio_pintura),
        int(var_aceite.get() * precio_aceite),
        int(var_mo.get() * precio_mo),
        int(var_ogp.get()),
        costo_fijo,
        valor_transformador,
        int(margen),
    )
    sql = "INSERT INTO  transformadores(id, cobre, pintura, aceite, mo ,ogp ,costos_fijos ,valor_transformador, margen)\
         VALUES(?,?,?,?,?,?,?,?,?)"
    cursor.execute(sql, data)
    conexion.commit()
    mostrar()


def modificar_trafo():
    global var_aceite, var_cobre, var_num_de_transformador, var_mo, var_ogp, var_pintura, valor_transformador, costo_fijo, conexion, margen
    cursor = conexion.cursor()
    margen = (
        int(valor_transformador)
        - int(var_aceite.get() * precio_aceite)
        - int(var_cobre.get() * precio_cobre)
        - int(var_mo.get() * precio_mo)
        - int(var_pintura.get() * precio_pintura)
        - int(costo_fijo)
        - int(var_ogp.get())
    )
    data = (
        int(var_cobre.get() * precio_cobre),
        int(var_pintura.get() * precio_pintura),
        int(var_aceite.get() * precio_aceite),
        int(var_mo.get() * precio_mo),
        int(var_ogp.get()),
        costo_fijo,
        valor_transformador,
        int(margen),
        int(var_num_de_transformador.get()),
    )
    sql = "UPDATE  transformadores SET cobre =?, pintura=?, aceite=?, mo=? ,ogp=?,costos_fijos=? ,valor_transformador=?, margen=? WHERE id = ?"
    cursor.execute(sql, data)
    conexion.commit()
    mostrar()


def buscar_id():
    global conexion, var_id_buscar
    cursor = conexion.cursor()
    mi_id = int(var_id_buscar.get())
    data = (mi_id,)
    sql = "SELECT * FROM transformadores WHERE id = ?"
    cursor.execute(sql, data)
    resultado = cursor.fetchall()  # guardo el conenido de la db en una tupla
    tree.delete(*tree.get_children())
    # vacio el tree para reemplazarlo por la db actualizada
    for i in resultado:  # con un for recorro la base de datos
        tree.insert(  # inserto cada elemento de la tupla  menos el 7 al tree
            "",
            "end",
            text=i[0],
            values=(
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[8],
            ),
        )


def borrar_id():
    global conexion, var_id_borrar
    cursor = conexion.cursor()
    mi_id = int(var_id_borrar.get())
    data = (mi_id,)
    sql = "DELETE FROM transformadores WHERE id = ?;"
    cursor.execute(sql, data)
    conexion.commit()

    mostrar()


def mostrar():
    global conexion
    cursor = conexion.cursor()
    sql = "SELECT * FROM transformadores"
    cursor.execute(sql)
    resultado = cursor.fetchall()  # guardo el conenido de la db en una tupla
    tree.delete(*tree.get_children())
    # vacio el tree para reemplazarlo por la db actualizada
    for i in resultado:  # con un for recorro la base de datos
        tree.insert(  # inserto cada elemento de la tupla  menos el 7 al tree
            "",
            "end",
            text=i[0],
            values=(
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[8],
            ),
        )


# definición de los botones de alta, modficar, buscar y ordenar:

alta = Button(
    principal, text="alta", command=alta_trafo, width=10, background="lightgreen"
)
alta.grid(row=5, column=1, pady=3)

modificar = Button(
    principal,
    text="modificar",
    command=modificar_trafo,
    width=10,
    background="#6CB7EB",
)
modificar.grid(row=5, column=2)

buscar_por_id = Button(
    principal, text="Filtrar por ID", command=buscar_id, width=10, background="yellow"
)
buscar_por_id.grid(row=1, column=5, padx=3, pady=3)

borrar_por_id = Button(
    principal, text="Borrar ID", command=borrar_id, background="red", width=10
)
borrar_por_id.grid(row=5, column=5, padx=3, pady=1)

quitar_filtros = Button(
    principal, text="Quitar Filtros", command=mostrar, width=10, background="#F4F1CE"
)
quitar_filtros.grid(row=3, column=5)

# Hago el treeview

tree = ttk.Treeview(principal)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")

tree.column("#0", width=90, anchor=CENTER)
tree.column("col1", width=90, anchor=CENTER)
tree.column("col2", width=90, anchor=CENTER)
tree.column("col3", width=90, anchor=CENTER)
tree.column("col4", width=90, anchor=CENTER)
tree.column("col5", width=90, anchor=CENTER)
tree.column("col6", width=90, anchor=CENTER)
tree.column("col7", width=90, anchor=CENTER)


tree.heading("#0", text="ID")
tree.heading("col1", text="Cobre")
tree.heading("col2", text="Pintura")
tree.heading("col3", text="Aceite")
tree.heading("col4", text="Mano de Obra")
tree.heading("col5", text="OGP")
tree.heading("col6", text="Costo fijo")
tree.heading("col7", text="Margen")

tree.grid(column=0, row=7, columnspan=7)

mostrar()  # llamo a la funcion mostrar para que el programase inicie con la base de datos actualizada en el tree

mainloop()  # loop de la interfaz
