''' Operator * unpacking '''
lista = [1, 2, 3, 4, 5]

print(lista)  # [1, 2, 3, 4, 5]
print('')

print(*lista)  # 1 2 3 4 5
print('')

lista_nueva = [6, 7, 8, 9, 10]
print(lista_nueva)  # [6, 7, 8, 9, 10]
print('')

lista_combinada = [*lista, *lista_nueva]
print(lista_combinada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('')

lista_combinada = [*lista, *lista_nueva, 'Hola', 'Pablo']
print(lista_combinada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Hola', 'Pablo']
print('')

punto1 = {'x': 2}
punto2 = {'y': 3}

nuevo_punto = {**punto1, **punto2}
print(nuevo_punto)  # {'x': 2, 'y': 3}
print('')

nuevo_punto = {**punto1, **punto2, 'z': 'Pablo'}
print(nuevo_punto)  # {'x': 2, 'y': 3, 'z': 'Pablo'}
print('')
