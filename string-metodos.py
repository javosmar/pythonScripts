curso = "Curso"
my_string = "La cuestion facil"

result = "{a} de {b} porque {a}".format(a = curso,b = my_string)    # Curso de La cuestion facil porque Curso

print(result)
print(result.lower())
print(result.upper())
print(result.title())

#----- BÚSQUEDA

cadena = 'cuestion'
pos = result.find(cadena)
print("Posición de la candena '{a}': {b}".format(a = cadena, b = pos))
cadenaBuscada = 'o'
count = result.count(cadenaBuscada)
print("Cantidad de repeticiones de '{a}': {b}".format(a = cadenaBuscada, b = count))

#------ SUSTITUCIÓN

nuevaCadena = result.replace('o','x')
print(nuevaCadena)

nuevaCadena = result.split(' ')
print(nuevaCadena)