# para funciones muy sencillas, de una sola línea

miFuncion = lambda valor_uno, valor_dos : valor_uno + valor_dos          # función anónima

formato = lambda sentencia : '¿{}?'.format(sentencia)
resultado = formato("como te va")
print(resultado)

no_valor = lambda : 10
resultado = no_valor()
print(resultado)

no_valor = lambda : print('algo debe hacer, no puede estar vacío')
resultado = no_valor()
print(resultado)