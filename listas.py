lista = ['hola','como','te','va']
print(lista)

#----- MODIFICAR LA LISTA

lista.append('capo')
print(lista)
lista.insert(2,'chaucha')
print(lista)
lista.remove('te')
print(lista)

lista.sort()
print(lista)

extraido = lista.pop()
print(lista)
print(extraido)

lista2 = ['que','se','cuenta']
lista.extend(lista2)
print(lista)