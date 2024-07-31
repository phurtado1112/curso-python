''' Listas '''

numeros = [1, 2, 3, 4, 5]

print(numeros[0])  # 1
print(numeros[4])  # 5
print('')

letras = ['a', 'b', 'c', 'd', 'e']
print(letras)  # ['a', 'b', 'c', 'd', 'e']
print('')

palabras = ['Hola', 'Mundo', 'Cruel']
print(palabras)  # ['Hola', 'Mundo', 'Cruel']
print('')

booleanos = [True, False, True]
print(booleanos)  # [True, False, True]
print('')

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('')

ceros = [0] * 5
print(ceros)  # [0, 0, 0, 0, 0]
print('')

ceros_unos = [0, 1] * 5
print(ceros_unos)  # [0, 0, 0, 0, 0]
print('')

alfanumericos = numeros + letras
print(alfanumericos)  # [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print('')

rango = list(range(10))
print(rango)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('')

rango_a_diez = list(range(1, 11))
print(rango_a_diez)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('')

chars = list('Hola Mundo')
print(chars)  # ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
print('')
