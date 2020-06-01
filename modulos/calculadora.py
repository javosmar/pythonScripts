#!/usr/bin/python3

"""
Descripción de lo que hace le módulo, a qué contexto le corresponde
"""

__autor__ = "El autor"
__copyright__ = "Copyright 2020, El autor"
__credits__ = "Código facilito"

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "El autor"
__email__ = "mail@gmail.com"
__status__ = "Developer"

def suma(num1,num2):
    """Devuelve la suma de 2 números"""
    return num1 + num2

def resta(num1,num2):
    """ Devuelve la resta de 2 números"""
    return num1 - num2

def multip(num1,num2):
    """Devuelve el producto de 2 números"""
    return num1 * num2

def div(num1,num2):
    """Devuelve el cociente de 2 números"""
    return num1 / num2

def saluda():
    print("Saluda")

if __name__ == "__main__":      # indica que no se ejecute al ser importado, solo si es ejecutado como main
    saluda()