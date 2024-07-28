''' funciones en Python '''

# def nombre_funcion(parametros):
#     instrucciones
#     return valor

nombre = 'Pablo'
apellido = 'Hurtado'


def saludar(nombre='Juan', apellido='Perez'):
    print("Hola, bienvenido a Python")
    print(f'Bienvenido {nombre}, {apellido}')


saludar(nombre, apellido)

saludar('Chanchito', 'Feliz')

saludar(apellido='Gomez', nombre='Ana')
