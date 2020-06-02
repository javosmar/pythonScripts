class Circulo:
    pi = 3.141596               # Variable de clase

    def __init__(self,radio):
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * self.pi
    

circulo1 = Circulo(3)
print(circulo1.area())
print(circulo1.__dict__)        # diccionario de variables en la clase
print(circulo1.pi)
print(Circulo.pi)