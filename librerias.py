"""
import random

valor = random.randint(0,10)        # genero un valor aleatorio

lista = [True,"String",23,False]
valor = random.choice(lista)        # elijo un elemento al azar de la lista

print(valor)

random.shuffle(lista)               # desordeno los elementos de la lista
print(lista)

#------------------------
import datetime

print(datetime.datetime.now())      # muestro la fecha y hora actual

#-----------------------
import sys
import time

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r%d %%" %i)  # genero la carga porcentual (como al descargar un archivo)
    sys.stdout.flush()

"""

# pasando parámetros al llamar a la librería

import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Es necesario colocar por lo menos un elemento")
    else:
        if sys.argv[1] == 'help':
            print("Contactar al desarrollador")
        else:
            print(sys.argv[1])