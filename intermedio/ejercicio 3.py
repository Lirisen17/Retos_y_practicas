

class Vehiculos:
    def __init__(self,color, matricula, velocidad_maxima):
        self.color = color
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima
           
    def imprimir(self, *args):
        print ("El color del vehiculo es:",self.color)
        print ("La matricula del vehiculo es:",self.matricula)
        print ("La velocidad del vehiculo es:",self.velocidad_maxima)
        
class Trenes(Vehiculos):
    def __init__(self,color, matricula, velocidad_maxima,peso):
        self.peso = peso
        super().__init__(color, matricula, velocidad_maxima)
    def imprimir(self):
        print("el peso es:",self.peso)
        super().imprimir(self)
        
        

tren = Trenes("Negro", 65421, 200,23)
auto = Vehiculos("rojo", 123,12)
tren_2 = Trenes("azul",122,121,1233)

auto.imprimir()
tren.imprimir()
tren_2.imprimir()

