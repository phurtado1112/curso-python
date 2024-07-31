''' Agregando y eliminando elementos de una lista '''
mascotas = ['perro', 'gato', 'loro', 'pez', 'gato', 'perro']

# insert() agrega un elemento en una posición específica
mascotas.insert(2, 'conejo')
print(mascotas)  # ['perro', 'gato', 'conejo', 'loro', 'pez', 'gato', 'perro']
print('')

# append() agrega un elemento al final de la lista
mascotas.append('tortuga')
# ['perro', 'gato', 'conejo', 'loro', 'pez', 'gato', 'perro', 'tortuga']
print(mascotas)
print('')

# remove() elimina la primera ocurrencia de un elemento
mascotas.remove('gato')
# ['perro', 'conejo', 'loro', 'pez', 'gato', 'perro', 'tortuga']
print(mascotas)
print('')

# pop() elimina un elemento en una posición específica
mascotas.pop()  # ['perro', 'conejo', 'loro', 'pez', 'gato', 'perro']
print(mascotas)
print('')

mascotas.pop(0)  # ['conejo', 'loro', 'pez', 'gato', 'perro']
print(mascotas)
print('')

# del elimina un elemento en una posición específica
del mascotas[1]  # ['perro', 'loro', 'pez', 'gato', 'perro']
print(mascotas)
print('')

# clear() elimina todos los elementos de la lista
mascotas.clear()
print(mascotas)  # []
print('')
