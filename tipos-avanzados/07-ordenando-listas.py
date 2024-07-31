''' Ordenando listas '''
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(numeros)  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print('')

numeros.sort()
print(numeros)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print('')

numeros.sort(reverse=True)
print(numeros)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
print('')

# sorted() crea una nueva lista ordenada
sorted_numeros = sorted(numeros)
print(sorted_numeros)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print('')

# sorted() también puede ordenar cadenas inverso
sorted_numeros = sorted(numeros, reverse=True)
print(sorted_numeros)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
print('')

usuarios = [[4, "Carlos"], [2, "Ana"], [3, "Beto"], [1, "Diana"]]
usuarios.sort()
print(usuarios)  # [[1, 'Diana'], [2, 'Ana'], [3, 'Beto'], [4, 'Carlos']]
print('')

usuarios = [["Carlos", 4], ["Ana", 2], ["Beto", 3], ["Diana", 1]]
usuarios.sort()
print(usuarios)  # [['Ana', 2], ['Beto', 3], ['Carlos', 4], ['Diana', 1]]
print('')


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)  # [['Diana', 1], ['Ana', 2], ['Beto', 3], ['Carlos', 4]]
print('')

usuarios.sort(key=ordena, reverse=True)
print(usuarios)  # [['Diana', 1], ['Ana', 2], ['Beto', 3], ['Carlos', 4]]
print('')

usuarios.sort(key=lambda elemento: elemento[1])
print(usuarios)  # [['Diana', 1], ['Ana', 2], ['Beto', 3], ['Carlos', 4]]
print('')
