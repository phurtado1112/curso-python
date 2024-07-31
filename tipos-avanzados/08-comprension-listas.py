''' compension de listas '''

usuarios = [["Carlos", 4], ["Ana", 2], ["Beto", 3], ["Diana", 1]]

nombre = []
for usuario in usuarios:
    nombre.append(usuario[0])
print(nombre)  # ['Carlos', 'Ana', 'Beto', 'Diana']
print('')

# map
nombre = [usuario[0] for usuario in usuarios]
print(nombre)  # ['Carlos', 'Ana', 'Beto', 'Diana']
print('')

# filtrar filter
nombre = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombre)  # ['Carlos', 'Beto']
print('')

# filtrar y transformar - lista de compresion
nombre = [usuario[0].upper() for usuario in usuarios if usuario[1] > 2]
print(nombre)  # ['CARLOS', 'BETO']
print('')

# map y filter
nombre = list(map(lambda usuario: usuario[0], usuarios))
print(nombre)  # ['Carlos', 'Ana', 'Beto', 'Diana']
print('')

# map y filter
nombre = list(map(lambda usuario: usuario[0], filter(
    lambda usuario: usuario[1] > 2, usuarios)))
print(nombre)  # ['Carlos', 'Beto']
print('')

# filter
nombre = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombre)  # [['Carlos', 4], ['Beto', 3]]
print('')
