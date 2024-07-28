''' Operador for '''

for i in range(5):
    print(i, i * 'Hola mundo ')

print('')

buscar = 3

for numero in range(5):
    if numero == buscar:
        print('Número encontrado', numero)
        break
print('')

buscar = 10

for numero in range(5):
    if numero == buscar:
        print('Número encontrado', numero)
        break
    else:
        print('Número no encontrado')

print('')

for char in 'Ultimate Python Course':
    print(char)
