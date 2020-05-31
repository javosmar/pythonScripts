def generador(*args):               # Crea objetos sin almacenarlos en RAM
    for valor in args:
        yield valor * 10, True      # devuelve los valores sin terminar la función
                                    # permite iteración

for valor1,valor2 in generador(1,2,3,4,5,6):
    print(valor1,valor2)