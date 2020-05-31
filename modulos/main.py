"""se recomienda importar funciones puntuales
    para saber qué funciones vienen de afuera"""

# importando la librería completa
#import calculadora

# importando funciones de una librería
#from calculadora import suma,resta
#from calculadora import multip
#from calculadora import div as func1

# importando todo de calculadora
from calculadora import *

resultado = suma(1,3)
resultado2 = resta(20,3)
print(resultado)
print(resultado2)
print(func1(40,3))