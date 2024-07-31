''' Tuplas '''
numeros = (1, 2, 3, 4, 5)
print(numeros)
print('')

# agregar otra tupla
numeros = numeros + (6, 7, 8)
print(numeros)
print('')

# converti lista a tupla
punto = tuple([1, 2])
print(punto)
print('')

# agregar un elemento a la tupla
# numeros.append(9) # AttributeError: 'tuple' object has no attribute 'append'
# print(numeros)
# print('')


menos_numeros = numeros[:2]  # (1, 2)
print(menos_numeros)
print('')

menos_numeros = numeros[:3]  # (1, 2, 3)
print(menos_numeros)
print('')

# desempaquetar tuplas
primero, segundo, *otros = numeros
print(primero, segundo, otros)  # 1 2 [3, 4, 5, 6, 7, 8]
print('')

for numero in numeros:
    print(numero)
print('')

# numero[4] = 7  # TypeError: 'tuple' object does not support item assignment
# print(numeros)
# print('')

lista_numeros = list(numeros)
print(lista_numeros)
print('')
lista_numeros[4] = 7
print(lista_numeros)
print('')
lista_numeros[6] = 'Otro_numero'
print(lista_numeros)
print('')
