"""
def suma(*args):                                                 # *args  -> n valores -> tuplas
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado  

resultado = suma(10,50,60)
print(resultado)
"""

def suma(**kwargs):                                             # **kwargs -> n valores -> diccionarios                 
    valor = kwargs.get('valor','No contiene el valor')
    print(valor)

resultado = suma(valor = 'Edu', x = 2, y = 5, z = True)
print(resultado)