from tkinter import *
from tkcalendar import *

root = Tk()

calendario = Calendar(root, selectmode="day", background="blue", selectbackground="red")
calendario.grid(row=1, column=1)


def imprimir(calendario):
    fecha = calendario.get_date()
    print(fecha)


enviar = Button(
    root, text="Imprimir fecha seleccionada", command=lambda: imprimir(calendario)
)
enviar.grid(row=2, column=1)

root.mainloop()
