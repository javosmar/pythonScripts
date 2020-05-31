diccionario = {'a':55, 3:"hola", (1,2):False}  # Las claves deben ser inmutables (entero, string o tupla)
print(diccionario)

#----- AGREGAR O MODIFICAR

diccionario['new_key'] = "valor nuevo"
print(diccionario)

diccionario['a'] = False
print(diccionario)

#----- OBTENER VALOR A PARTIR DE LLAVE

variable = diccionario['new_key']
print(variable)

variable = diccionario.get('z','No encontrado')
print(variable)

#----- ELIMINAR PAR CLAVE-VALOR

del diccionario[(1,2)]
print(diccionario)

#----- OBTENER LA LISTA DE LLAVES O VALORES

llaves = list(diccionario.keys())
print(llaves)
valores = list(diccionario.values())
print(valores)

#----- EXTENDER DICCIONARIO

diccionario2 = {'z':"tu",'asd':1234.4}
# diccionario['z'] = diccionario2['z']
# diccionario['asd'] = diccionario2['asd']
diccionario.update(diccionario2)
print(diccionario)

