''' Operador while '''

numero = 1

while numero < 100:
    print(numero)
    numero *= 2

print('')

comando = ''

while comando.lower() != 'salir':
    comando = input('Introduce un comando $: ')
    print('Has introducido el comando:', comando)
