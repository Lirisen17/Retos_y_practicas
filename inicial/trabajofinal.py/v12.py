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
    TclError,
    DoubleVar,
    ttk,
)

# import sqlite3
from sqlite3 import connect, IntegrityError
from pandas import read_sql_query
from matplotlib.pyplot import bar, gca, title, show
from re import match

principal = Tk()

# declaración de todas las variables del programa:
var_ordenar_str = StringVar()
id = StringVar()
var_cobre = DoubleVar()
var_aceite = DoubleVar()
var_pintura = DoubleVar()
var_ogp = DoubleVar()
var_mo = DoubleVar()
var_id_buscar = StringVar()
var_id_borrar = StringVar()
costo_fijo = 400
valor_transformador = 3750
precio_cobre = 16
precio_pintura = 10
precio_aceite = 2
precio_mo = 2
margen = 0
w = 14

# declaracion de las function que van a ser llamadas por los botones:


def alta_trafo(
    var_aceite,
    var_cobre,
    id,
    var_mo,
    var_ogp,
    var_pintura,
    valor_transformador,
    costo_fijo,
    conexion,
    margen,
):
    try:
        valor = str(id.get())
        patron = "^[0-9]+$"
        if match(patron, valor):  # Uso regex para validar la id
            cursor = conexion.cursor()
            margen = (
                float(valor_transformador)
                - float(var_aceite.get() * precio_aceite)
                - float(var_cobre.get() * precio_cobre)
                - float(var_mo.get() * precio_mo)
                - float(var_pintura.get() * precio_pintura)
                - float(costo_fijo)
                - float(var_ogp.get())
            )  # Calculo el margen restandoselo el valor del transformador a todos los costos
            data = (
                float(id.get()),
                round(float(var_cobre.get() * precio_cobre), 2),
                round(float(var_pintura.get() * precio_pintura), 2),
                round(float(var_aceite.get() * precio_aceite), 2),
                round(float(var_mo.get() * precio_mo), 2),
                round(float(var_ogp.get()), 2),
                costo_fijo,
                valor_transformador,
                round(float(margen), 2),
            )  # guardo todos los valores en una variable
            sql = "INSERT INTO  transformadores(id, cobre, pintura, aceite, mo ,ogp ,costos_fijos ,valor_transformador, margen)\
                VALUES(?,?,?,?,?,?,?,?,?)"
            cursor.execute(
                sql, data
            )  # ejecuto la sentencia sql con los valores guardados anteriormente en data
            conexion.commit()
            mostrar(conexion)
            messagebox.showinfo(
                message="Transformador registrado correctamente!", title="Mensaje"
            )
        else:
            messagebox.showinfo(
                message="El campo id solo admite números", title="Error"
            )
    except TclError:
        messagebox.showinfo(
            message="Valores invalidos. Recuerda que solo se admiten numeros reales!",
            title="Error",
        )
    except IntegrityError:
        messagebox.showinfo(message="Este transformador ya existe!", title="Error")


def modificar_trafo(
    var_aceite,
    var_cobre,
    id,
    var_mo,
    var_ogp,
    var_pintura,
    valor_transformador,
    costo_fijo,
    conexion,
    margen,
):
    try:  # uso try para capturar errores
        valor = str(id.get())
        patron = "^[0-9]+$"  # uso regex para validar el ingreso de id
        if match(patron, valor):
            cursor = conexion.cursor()
            margen = (
                float(valor_transformador)
                - float(var_aceite.get() * precio_aceite)
                - float(var_cobre.get() * precio_cobre)
                - float(var_mo.get() * precio_mo)
                - float(var_pintura.get() * precio_pintura)
                - float(costo_fijo)
                - float(var_ogp.get())
            )  # Calculo el margen restandoselo el valor del transformador a todos los costos
            data = (
                round(float(var_cobre.get() * precio_cobre), 2),
                round(float(var_pintura.get() * precio_pintura), 2),
                round(float(var_aceite.get() * precio_aceite), 2),
                round(float(var_mo.get() * precio_mo), 2),
                round(float(var_ogp.get()), 2),
                costo_fijo,
                valor_transformador,
                round(float(margen), 2),
                int(id.get()),
            )  # guardo todos los valores en una variable
            sql = "UPDATE  transformadores SET cobre =?, pintura=?, aceite=?, mo=? ,ogp=?,costos_fijos=? ,valor_transformador=?, margen=? WHERE id = ?"
            cursor.execute(
                sql, data
            )  # ejecuto la sentencia sql con los valores guardados anteriormente en data
            conexion.commit()
            mostrar(conexion)
        else:
            messagebox.showinfo(
                message="El campo id solo admite números", title="Error"
            )
    except TclError:
        messagebox.showinfo(
            message="Valores invalidos. Recuerda que solo se admiten numeros reales!",
            title="Error",
        )
    else:  # este else corresponde al try. Se ejecuta siempre que no entre en ninguna except
        messagebox.showinfo(
            message="Transformador modificado correctamente!", title="Mensaje"
        )


def buscar_id(conexion, var_id_buscar):
    valor = str(var_id_buscar.get())
    patron = "^[0-9]+$"
    if match(patron, valor):  # uso regex para validar el ingreso de id
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
    else:
        messagebox.showinfo(message="El campo id solo admite números", title="Error")


def borrar_id(conexion, var_id_borrar):
    valor = str(var_id_borrar.get())
    patron = "^[0-9]+$"
    if match(patron, valor):  # uso regex para validar el ingreso de id
        contrador_inicial = contador_registros(conexion)
        cursor = conexion.cursor()
        mi_id = int(var_id_borrar.get())
        data = (mi_id,)
        sql = "DELETE FROM transformadores WHERE id = ?;"
        cursor.execute(sql, data)
        conexion.commit()
        mostrar(conexion)
        contador_final = contador_registros(conexion)
        if (
            contrador_inicial == contador_final
        ):  # si es true quiere decir que no elimino ningun registro durante la ejecucion de la funcion
            messagebox.showinfo(message="Registro no encontrado.", title="Error")
        else:
            messagebox.showinfo(message="Registro Eliminado!", title="Completado")
    else:
        messagebox.showinfo(message="El campo solo admite números.", title="Error")


def mostrar(conexion):
    global var_ordenar_str  # traigo la variable del combobox
    aux = str(var_ordenar_str.get())
    if aux == "":  # condicional para que por defecto use el id para ordenar
        aux = "id"
    cursor = conexion.cursor()
    sql = (
        "SELECT * FROM transformadores ORDER BY " + aux + " ASC"
    )  # trate de hacerlo con ? y reemplazarlo con la variable aux en la linea de .execute pero no me funciono
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


# La funcion contador la uso para auxiliarme en la funcion graficos y en la borrar_id.
def contador_registros(con):
    sql = "SELECT * FROM transformadores"
    cursor = con.cursor()
    cursor.execute(sql)
    conexion.commit()
    return len(cursor.fetchall())


# uso pandas para seleccionar y guardar en una variable la base de datos y mostrarla en un grafico con matplot
def graficos(con):
    try:
        df = read_sql_query(
            "SELECT id, margen from transformadores", con, index_col="id"
        )

        df["margen"].plot(kind="bar")

        bar(
            range(contador_registros(con)),
            df["margen"],
            align="center",
            color=["blue", "red", "lightgreen", "orange", "yellow", "purple"],
            edgecolor="black",
        )
        ax = gca()
        ax.set_facecolor("lightgrey")
        ax.set_ylabel("Margen")
        title("Margen de ganancia de cada transformador")
        show()
    except:
        messagebox.showinfo(
            message="La base de datos esta vacia. No hay graficos para mostrar.",
            title="Error",
        )


# crear base y tabla sqlite
def crear_conexion():
    con = connect("base_trafos.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS transformadores(id string PRIMARY KEY NOT NULL, cobre real,pintura real, aceite real, mo real, ogp real, costos_fijos real,valor_transformador real, margen real)"
    cursor.execute(sql)
    con.commit()


conexion = crear_conexion()
crear_tabla(conexion)

# declaracion de los entry para que el usuario cargue datos:


principal.geometry("729x365")  # tamaño de ventana
principal.resizable(width=False, height=False)  # deshabilito la modificacion del tamaño
principal.title("Calculadora de costos en transformadores")

numero_transformador = Entry(principal, textvariable=id, width=w)
numero_transformador.grid(row=1, column=1)

cobre = Entry(principal, textvariable=var_cobre, width=w)
cobre.grid(row=2, column=1)

aceite = Entry(principal, textvariable=var_aceite, width=w)
aceite.grid(row=3, column=1)

pintura = Entry(principal, textvariable=var_pintura, width=w)
pintura.grid(row=4, column=1)

ogp = Entry(principal, textvariable=var_ogp, width=w)
ogp.grid(row=1, column=3)

mo = Entry(principal, textvariable=var_mo, width=w)
mo.grid(row=2, column=3)

id_buscar = Entry(principal, textvariable=var_id_buscar, width=w)
id_buscar.grid(row=1, column=6)

id_borrar = Entry(principal, textvariable=var_id_borrar, width=w)
id_borrar.grid(row=3, column=6)


# declaración de los labels que le indican al usuario que datos ingresar:
label_id = Label(principal, text="ID del Transformador: ")
label_id.grid(row=1, column=0, sticky="W")

label_cobre = Label(principal, text="Kg de cobre: ")
label_cobre.grid(row=2, column=0, sticky="W")

label_aceite = Label(principal, text="Lts de Aceite:")
label_aceite.grid(row=3, column=0, sticky="W")

label_pintura = Label(principal, text="Lts de Pintura:")
label_pintura.grid(row=4, column=0, sticky="W")

label_ogp = Label(principal, text="Precio de OGPs: ")
label_ogp.grid(row=1, column=2, sticky="W")

label_mo = Label(principal, text="Hs Mano de obra:")
label_mo.grid(row=2, column=2, sticky="W")

label_costo_fijo = Label(principal, text="Costo fijo promedio:")
label_costo_fijo.grid(row=3, column=2, sticky="W")

lavel_valor_costo_fijo = Label(
    principal, text=costo_fijo, borderwidth=3, relief="groove", width=12
)
lavel_valor_costo_fijo.grid(row=3, column=3, pady=3)

ordenar_por = Label(principal, text="Ordenar por", width=12)
ordenar_por.grid(row=4, column=3)


var_ordenar = ttk.Combobox(principal, textvariable=var_ordenar_str, state="readonly")
var_ordenar.grid(column=3, row=5)
var_ordenar["values"] = ("id", "cobre", "aceite", "pintura", "ogp", "margen")
var_ordenar.set("id")

# definición de los botones de alta, modficar, buscar,borrar, sacar filtro y graficar:

alta = Button(
    principal,
    text="alta",
    command=lambda: alta_trafo(
        var_aceite,
        var_cobre,
        id,
        var_mo,
        var_ogp,
        var_pintura,
        valor_transformador,
        costo_fijo,
        conexion,
        margen,
    ),
    width=10,
    background="lightgreen",
)
alta.grid(row=5, column=1, pady=3)

modificar = Button(
    principal,
    text="modificar",
    command=lambda: modificar_trafo(
        var_aceite,
        var_cobre,
        id,
        var_mo,
        var_ogp,
        var_pintura,
        valor_transformador,
        costo_fijo,
        conexion,
        margen,
    ),
    width=10,
    background="#6CB7EB",
)
modificar.grid(row=5, column=2)

buscar_por_id = Button(
    principal,
    text="Filtrar por ID",
    command=lambda: buscar_id(conexion, var_id_buscar),
    width=10,
    background="yellow",
)
buscar_por_id.grid(row=1, column=5, padx=3, pady=3)

borrar_por_id = Button(
    principal,
    text="Borrar ID",
    command=lambda: borrar_id(conexion, var_id_borrar),
    background="red",
    width=10,
)
borrar_por_id.grid(row=3, column=5, padx=3, pady=1)

quitar_filtros = Button(
    principal,
    text="Actualizar",
    command=lambda: mostrar(conexion),
    width=10,
    background="#F4F1CE",
)
quitar_filtros.grid(row=5, column=5)

graficar = Button(
    principal,
    text="Grafico Margenes",
    command=lambda: graficos(conexion),
    width=13,
    background="#E68849",
)
graficar.grid(row=5, column=0)


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

tree.grid(column=0, row=7, columnspan=7, padx=3)

mostrar(conexion)
# llamo a la funcion mostrar para que el programase inicie con la base de datos actualizada en el tree

mainloop()  # loop de la interfaz


# Nicolás Campanella Lerra
# Curso 999188618
# Python 3 - Nivel Inicial
