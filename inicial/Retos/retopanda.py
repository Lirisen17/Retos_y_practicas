"""Cree una tabla de excel con datos de precio - cantidad, tome los datos con pandas y grafiquelos con matplotlib"""


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("data.xlsx", index_col="Producto")


def pxq(fila):
    total = fila["Precio"] * fila["Cantidad"]
    return total


df["total"] = df.apply(pxq, axis=1)


df["Precio"].plot()
plt.show()
