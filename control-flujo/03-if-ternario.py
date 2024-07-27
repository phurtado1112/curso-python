''' uso del operador ternario '''

# if else

edad = 22

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

print('Fin del programa')
print('')

edad = 15

if edad >= 18:
    mensaje = 'Eres mayor de edad'
else:
    mensaje = 'Eres menor de edad'

print(mensaje)
print('Fin del programa')
print('')


# if ternario
edad = 22

print('Eres mayor de edad') if edad >= 18 else print('Eres menor de edad')
