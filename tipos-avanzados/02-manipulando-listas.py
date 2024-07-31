''' Manipulando listas '''
mascotas = ['perro', 'gato', 'pez', 'conejo', 'hamster']
print(mascotas)
print('')

print(mascotas[0])  # perro
print(mascotas[4])  # hamster
print('')

mascotas[2] = 'pajaro'
print(mascotas)  # ['perro', 'gato', 'pajaro', 'conejo', 'hamster']
print('')

print(mascotas[1:3])  # ['gato', 'pajaro']
print('')

print(mascotas[:2])  # ['perro', 'gato']
print('')
print(mascotas[2:])  # ['pajaro', 'conejo', 'hamster']
print('')
print(mascotas[:])  # ['perro', 'gato', 'pajaro', 'conejo', 'hamster']
print('')
print(mascotas[-1])  # hamster
print('')
print(mascotas[-3])  # pajaro
print('')

print(mascotas[1::2])  # ['gato', 'conejo']
print('')
print(mascotas[::2])  # ['perro', 'pajaro', 'hamster']
print('')

numeros = range(21)
print(list(numeros[::2]))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print('')
print(list(numeros[1::2]))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print('')
