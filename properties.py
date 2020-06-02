class User:
    def __init__(self,nombre,email,password):
        self.nombre = nombre
        self.email = email
        self.__password = self.__generarPass(password)    # El doble __ indica que es un atributo privado

    
    def __generarPass(self,password):                   # Método privado
        return password.upper()

    def getPassword(self):
        return self.__password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,valor):
        self.__password = self.__generarPass(valor)

usuario1 = User('Eduardo','edu@gmail.com','qwerty')
print(usuario1.getPassword())
print(usuario1.password)            # permite acceder al atributo privado como una propiedad
usuario1.password = "otropassword"  # permite cambiar el atributo privado como una propiedad
print(usuario1.password)