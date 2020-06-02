class User:
    def __init__(self,nombre,email,password):
        self.nombre = nombre
        self.email = email
        self.__password = self.__generarPass(password)    # El doble __ indica que es un atributo privado

    
    def __generarPass(self,password):                   # Método privado
        return password.upper()

    def getPassword(self):
        return self.__password

usuario1 = User('Eduardo','edu@gmail.com','qwerty')
print(usuario1.getPassword())