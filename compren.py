lista = [valor for valor in range(0,101) if valor % 2 == 0]       # List Comprehension: valor a agregar a la lista, ciclo for y se obtiene la lista cargada
                                                                  # % obtiene el resto de una división


tupla = tuple((valor for valor in range(0,101)  if valor % 2 != 0))
#print(tupla)

diccionario = {indice:valor for indice,valor in enumerate(lista) if indice < 10}
print(diccionario)