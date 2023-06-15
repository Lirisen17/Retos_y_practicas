import sqlite3
import re
import pymongo
# ##############################################
# MODELO
# ##############################################

class Db():
    
    def mongo_set(self):        
            client = pymongo.MongoClient('localhost',27017)
            database = client['dbMongo']  
            collection = database['TablaMongo'] 
            return collection
    def sql_set(self):           
            con = sqlite3.connect("mibase.db")
            cursor = con.cursor()
            sql = """CREATE TABLE IF NOT EXISTS productos 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto varchar(20) NOT NULL,
                cantidad real,
                precio real)
                """
            cursor.execute(sql)
            con.commit()
        
class Abmc(Db):
    def __init__(self, ): pass

    def alta(self, producto, cantidad, precio, tree,base):        
        cadena = producto
        patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena
        if(re.match(patron, cadena)):            
                       
            if base == "Mongo DB":
                tabla_mongo=super().mongo_set()                     
                mi_dict = {"producto":producto,"cantidad":cantidad,"precio":precio}                                
                registro = tabla_mongo.insert_one(mi_dict)    
            else:
                super().sql_set() 
                print(producto, cantidad, precio)
                con=sqlite3.connect("mibase.db")
                data=(producto, cantidad, precio)  
                cursor=con.cursor()                
                sql="INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
                cursor.execute(sql, data)
                con.commit()
                print("Estoy en alta todo ok")
            self.actualizar_treeview(tree,base)
        else:
            print("error en campo producto")

    def actualizar_treeview(self, mitreview,base):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        if base == "Mongo DB":
            tabla_mongo=super().mongo_set() 
            resultados = tabla_mongo.find()
            for n in resultados:                       
                mitreview.insert("", 0, text=n['_id'], values=(n['producto'], n['cantidad'], n['precio']))
            


        else:
            sql = "SELECT * FROM productos ORDER BY id ASC"
            con=sqlite3.connect("mibase.db")
            cursor=con.cursor()
            datos=cursor.execute(sql)

            resultado = datos.fetchall()
            for fila in resultado:
                print(fila)
                mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))



