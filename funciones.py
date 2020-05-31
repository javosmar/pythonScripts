def factorial_numero(numero):
    factorial = 1
    while numero > 0:
        factorial *= numero
        numero -= 1
    return factorial

resultado = factorial_numero(5)
print(resultado)