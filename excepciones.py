try:
    lista = [1,2,3,4]
    pos = 6
    print(lista[pos])
except IndexError as error:
    print("No se pudo obtener el elemento {} de la lista".format(pos))
except ZeroDivisionError as error:
    print(error)
    print("No se puede dividir por cero")
except Exception as error:
    print(error)
    print("Ups, algo salió mal")

print("fin del script")