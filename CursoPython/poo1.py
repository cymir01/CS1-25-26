class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self): # self = referencia a la propia instancia de clase
        self.enmarcha = True

    def estado(self):
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"


miCoche = Coche()
print("El largo del chasis es", miCoche.largoChasis)
miCoche.arrancar()
print(miCoche.estado())

