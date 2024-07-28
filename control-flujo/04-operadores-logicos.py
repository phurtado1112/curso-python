''' Operadores lógicos and, or, not '''

gas = True
encendido = True

if gas and encendido:
    print('El coche arranca')

print('')

gas = True
encendido = False

if gas and encendido:
    print('El coche arranca')
else:
    print('El coche no arranca')

print('')

gas = True
encendido = False

if gas and not encendido:
    print('El coche arranca')
else:
    print('El coche no arranca')

print('')

gas = True
encendido = True
edad = 25

if gas and encendido and edad >= 18:
    print('El coche arranca', edad)
else:
    print('El coche no arranca')

print('')

gas = True
encendido = True
edad = 22

if gas and (encendido or edad >= 18):
    print('El coche arranca', edad)
else:
    print('El coche no arranca')

print('')

gas = True
encendido = False
edad = 22

if gas and (encendido or edad >= 18):
    print('El coche arranca', edad)
else:
    print('El coche no arranca')

print('')
