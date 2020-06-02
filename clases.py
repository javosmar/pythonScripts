class Objeto:
    def __init__(self,color = 'Negro',ancho = 0.5,largo = 17,isVacio = False):
        self.color = color
        self.ancho = ancho
        self.largo = largo
        self.isVacio = isVacio
    def accion(self):
        print("Método de la función")
    def accion2(self):
        self.color = 'negro'
    def accion3(self):
        self.accion2()
    def mostrarAtributos(self):
        print(self.color)
        print(self.ancho)
        print(self.largo)
        print(self.isVacio)


try:
    objeto1 = Objeto('Azul',0.7,13,True)
    objeto1.mostrarAtributos()
except AttributeError as error:
    print(error)
    print("Atributo inexistente")
except Exception as error:
    print(error)