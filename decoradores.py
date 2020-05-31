# A, B y C son funciones
# A recibe como parámetro B para poder crear C

"""
def decorador(func):                            # A(B)
    def nuevaFuncion(*args, **kwargs):          # se obtiene una función flexible en cuanto a los argumentos
        print("vamos a ejecutar la función")    # Código previo a la ejecución de func
        func(*args, **kwargs)
        print("función ejecutada")              # Código posterior a la ejecución de func
    return nuevaFuncion                         # C

@decorador
def saluda():
    print("Hola mundo")

@decorador
def suma(val1, val2):
    print(val1 + val2)


saluda()
suma(10,20)
"""
"""
def decorador(func):                            # A(B)
    def beforeAction():
        print("vamos a ejecutar la función")

    def afterAction():
        print("función ejecutada")

    def nuevaFuncion(*args, **kwargs):          # se obtiene una función flexible en cuanto a los argumentos
        beforeAction()                          # Código previo a la ejecución de func
        resultado = func(*args, **kwargs)
        afterAction()                           # Código posterior a la ejecución de func
        return resultado
    return nuevaFuncion                         # C

@decorador
def saluda():
    print("Hola mundo")

@decorador
def suma(val1, val2):
    return val1 + val2

#saluda()
resultado = suma(10,20)
print(resultado)
"""

def decorador(isValid):
    def _decorador(func):                           # A(B)
        def beforeAction():
            print("vamos a ejecutar la función")

        def afterAction():
            print("función ejecutada")

        def nuevaFuncion(*args, **kwargs):          # se obtiene una función flexible en cuanto a los argumentos
            if isValid:
                beforeAction()                      # Código previo a la ejecución de func
            
            resultado = func(*args, **kwargs)
            
            afterAction()                           # Código posterior a la ejecución de func
            return resultado
        return nuevaFuncion                         # C
    return _decorador

@decorador(isValid = False)
def suma(val1, val2):
    return val1 + val2

#saluda()
resultado = suma(10,20)
print(resultado)