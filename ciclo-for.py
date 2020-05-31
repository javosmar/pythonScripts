lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
    pass

nuevo_rango = range(0,12)       # se genera una lista iterable del 0 al 11
for valor in nuevo_rango:
    pass

nuevo_rango = range(0,20,2)     # se genera una lista iterable del 0 al 19, con saltos de 2
for valor in nuevo_rango:
    pass

indice = 0
for valor in lista:
    pass

indice = 0
for indice,valor in enumerate(lista):
    pass#print(valor,"tiene el índice",indice)

for valor in range(0,len(lista)):
    pass#print(valor)

for valor in 'Curso de python en youtube':
    pass#print(valor)

diccionario = {'a':10,'b':20,'c':30}
for llave,valor in diccionario.items():
    print("la llave",llave,"tiene el valor de",valor)