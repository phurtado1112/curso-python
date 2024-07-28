''' Ejercios de funciones '''


def es_palindromo(palabra):
    ''' Determina si una palabra es palíndromo '''
    return palabra == palabra[::-1]


resultado = es_palindromo("abba")

print(resultado)  # True
print('')


def no_espacios(palabra):
    ''' Elimina los espacios de una palabra '''
    nueva_palabra = ''
    for letra in palabra:
        if letra != ' ':
            nueva_palabra += letra
    return nueva_palabra


def es_palindromo_espaniol(palabra):
    ''' Determina si una palabra es palíndromo '''
    palabra = no_espacios(palabra)
    return palabra.lower() == palabra[::-1].lower()


# print(no_espacios('Hola Mundo'))  # 'HolaMundo'
print(es_palindromo_espaniol("anita Lava la tina"))  # True
