

class Vehiculos:
    def __init__(self,color, matricula, velocidad_maxima):
        self.color = color
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima
    
    def imprimir(self):
        print ("El color del auto es:",self.color)
        print ("La matricula del auto es:",self.matricula)
        print ("La velocidad del auto es:",self.velocidad_maxima)
        


primer_vehiculo = Vehiculos("Rojo", 12345, 125)
segundo_vehiculo = Vehiculos("Azul", 78910, 70)
tercer_vehiculo = Vehiculos("Negro", 65421, 200)


primer_vehiculo.imprimir()
segundo_vehiculo.imprimir()
tercer_vehiculo.imprimir()
