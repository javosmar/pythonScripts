fruta = 'kiwi'

#----- IF

if fruta == 'kiwi':
    print(fruta)
elif fruta == 'manzana':
    print('es una manzana')
elif fruta == 'naranja':
    pass                            # para evitar el error al no haber acciones, se coloca 'pass'
else:
    print("no funca")

mensaje = "la fruta es kiwi" if fruta == "kiwi" else "no es kiwi"
print(mensaje)

#----- COMPROBAR VARIABLE VACÍA

variable = 'asd'
variable = None
if variable:                        # Cualquier variable vacía, devuelve un false
    print(True)
else:
    print(False)

variable2 = '123'
if variable or variable2:           # and, or
    print(True)                           
else:
    print(False)