def suma(val1,val2 = 12,val3 = 10):
    resultado = val1 + val2 + val3
    return resultado

def dividir(val1,val2 = 1):
    resultado = val1 // val2
    resto = val1 % val2
    return resultado,resto

#cadena = int(input("ingrese un valor:"))
resultado = dividir(13,val2 = 10)               # defino el valor de los parámetros al invocar a la función, 
#print(resultado)                                # sin importar el órden pero sabiendo el nombre de los argumentos que recibe la función
entero = resultado[0]
resto = resultado[1]
#print(entero)
#print(resto)

variable = suma                                 # meto una función en una variable
#print(variable(4,5))

def mostrar_resultado(funcion,val1,val2):                 # paso una función como parámetro
    print(funcion(val1,val2))

variable = suma
mostrar_resultado(variable,10,20)