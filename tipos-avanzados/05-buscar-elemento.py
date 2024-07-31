''' Buscar un elemento en una lista '''
mascotas = ['perro', 'gato', 'loro', 'pez', 'gato', 'perro']

print(mascotas.index('loro'))  # 2
print('')

if 'loro' in mascotas:
    print('loro está en la lista', mascotas.index(
        'loro'))  # loro está en la lista 2
print('')

print(mascotas.count('perro'))  # 2
print('')
