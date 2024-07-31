''' Diccioanrios '''
punto = {'x': 2, 'y': 3}
print(punto)  # {'x': 2, 'y': 3}
print('')

# acceder a un valor
print(punto['x'])  # 2
print('')
print(punto['y'])  # 3
print('')

# agregar un valor
punto['z'] = 4
print(punto)  # {'x': 2, 'y': 3, 'z': 4}
print('')

# print(punto['d'])  # KeyError: 'd'
if 'd' in punto:
    print(punto['d'])
else:
    print('No existe la llave "d"')
print('')

# llaves
print(punto.keys())  # dict_keys(['x', 'y', 'z'])
print('')

# valores
print(punto.values())  # dict_values([2, 3, 4])
print('')

# items
print(punto.items())  # dict_items([('x', 2), ('y', 3), ('z', 4)])
print('')

# get
print(punto.get('x'))  # 2
print('')
print(punto.get('d'))  # None
print('')
print(punto.get('d', 'No existe la llave "d"'))  # No existe la llave "d"
print('')
print(punto.get('d', 10))  # 10
print('')

# eliminar un valor
del punto['z']
print(punto)  # {'x': 2, 'y': 3}
print('')
# del punto['d']  # KeyError: 'd'
# del (punto['d'])  # KeyError: 'd'
# del (punto('x'))  # TypeError: 'dict' object is not callable
print('')
del (punto['x'])  # KeyError: 'x'
print(punto)  # {'y': 3}
print('')

punto['x'] = 2
print(punto)  # {'y': 3, 'x': 2}
print('')

# limpiar un diccionario
punto.clear()
print(punto)  # {}
print('')

for valor in punto:
    print(valor, punto[valor])
print('Llaves')

# or key in punto.keys():
#     print(key)
# print('Llaves')
# print('')

for value in punto:
    print(value)
print('Valores')
print('')

for key, value in punto.items():
    print(key, value)
print('')

usuarios = [
    {'id': 1, 'nombre': 'Juan'},
    {'id': 2, 'nombre': 'Ana'},
    {'id': 3, 'nombre': 'Pedro'},
    {'id': 4, 'nombre': 'Maria'}
]

for usuario in usuarios:
    print(usuario['nombre'])
print('')
