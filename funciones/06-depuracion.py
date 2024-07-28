''' Depuración de código '''


def largo(texto):
    print(len(texto))
    resultado = 0
    for letra in texto:
        resultado += 1
    return resultado


print(largo('Hola Mundo'))  # 1
