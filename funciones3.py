# definiendo frase como variable local
"""
def palindromo(frase):
    frase_limpia = frase.replace(' ','')
    return frase_limpia == frase_limpia[::-1]

sentencia = 'anita lava la tina'
resultado = palindromo(sentencia)
print(resultado)
"""
"""
# definiendo frase como variable global

def palindromo():
    nueva_frase = frase.replace(' ','')
    return nueva_frase == nueva_frase[::-1]

frase = 'anita lava la tina'
resultado = palindromo()
print(resultado)
"""

# modificando una variable global desde una función

def funcion():
    global frase                # para crear o modificar una variable global desde una funcion, se la menciona como global, sino 
                                # queda definida como local
    frase = "chau tu plata"

frase = 'anita lava la tina'
print(frase)
resultado = funcion()
print(frase)
