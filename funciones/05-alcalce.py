''' Alcance de las variables '''
saludo = 'Hola Globar'


def saludar():
    nombre = 'Juan'
    saludo = f'Hola {nombre}'
    print(saludo)


def saludar2():
    saludo = 'Hola Chanchito'
    print(saludo)

# print(saludo) # NameError: name 'saludo' is not defined


saludar()
print('')
saludar2()
print('')
print(saludo)
print('')
