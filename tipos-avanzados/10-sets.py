''' Sets '''
# un set es una colección desordenada de elementos únicos (NO REPETIBLES) y no indexados - pueden llamarse conjuntos o grupos
# se crean con llaves {}
primer = {1, 2, 2, 3, 4, 4, 5}
print(primer)  # {1, 2, 3, 4, 5}
print('')
primer.add(6)
print(primer)  # {1, 2, 3, 4, 5, 6}
print('')

primer.remove(2)  # si el elemento no existe, arroja un error
print(primer)  # {1, 3, 4, 5, 6}
print('')

segundo = [4, 5, 6, 7, 8]
segundo = set(segundo)
print(segundo)  # {4, 5, 6, 7, 8}
print('')

# operaciones con sets
print(primer | segundo)  # {1, 3, 4, 5, 6, 7, 8} - union
print('')

print(primer & segundo)  # {4, 5, 6} - intersección
print('')

print(primer - segundo)  # {1, 3} - diferencia
print('')
print(segundo - primer)  # {8, 7} - diferencia
print('')

print(primer ^ segundo)  # {1, 3, 7, 8} - diferencia simétrica
print('')

# métodos de sets
# segundo[0] = 9  # TypeError: 'set' object does not support item assignment
# print(segundo)
# print('')

if 4 in primer:
    print('El 4 está en el primer set')
print('')
