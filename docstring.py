""" Cómo documentar funciones (dentro de las funciones) """

def generador(*args):               # Crea objetos sin almacenarlos en RAM
    """
    Recibe n cantidad de números y regresa en número,
    además de regresar un valor booleano si el número es 
    mayor a 5
    """
    for valor in args:
        yield valor * 10, True      # devuelve los valores sin terminar la función
                                    # permite iteración

""" __doc__ es un método de las funciones que 
    devuelve lo documentado en las mismas """
"""
documentacion = generador.__doc__
nombre = generador.__name__
print(nombre,":",documentacion)
"""

"""
en el intérprete de python:
>>>from docstring import generador
>>>help(generador)
"""