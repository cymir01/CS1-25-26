class Coche():

    def __init__(self): #constructor = metodo especial que le da estado inicial a los objetos
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    
    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}")

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-----------Segundo objeto----------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.__ruedas = 2 #aqui introduce encapsulacion para evitar que una propiedad se modifique desde fuera de la clase
miCoche2.estado()
