''' Iterar listas '''

mascotas = ['perro', 'gato', 'loro', 'pez', 'conejo']

for mascota in mascotas:
    print(mascota)
print('')

# enumerate
for i, mascota in enumerate(mascotas):
    print(i, mascota)
print('')

for mascota in enumerate(mascotas):
    print(mascota)
print('')
