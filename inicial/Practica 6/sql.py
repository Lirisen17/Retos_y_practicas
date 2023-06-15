import mysql.connector

mibase = mysql.connector.connect(host="localhost", user="root", password="")

mi_cursor = mibase.cursor()
mi_cursor.execute("CREATE DATABASE mi_plantilla")
