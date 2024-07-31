''' Desempaquetar listas '''
numeros = [1, 2, 3, 4, 5]

# feo
uno = numeros[0]
dos = numeros[1]
tres = numeros[2]
cuatro = numeros[3]
cinco = numeros[4]

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print('')

# bonito
uno, dos, tres, cuatro, cinco = numeros
print(uno, dos, tres, cuatro, cinco)  # 1 2 3 4 5
print('')

# desempaquetar con *
uno, dos, *tres = numeros
print(uno, dos, tres)  # 1 2 [3, 4, 5]
print('')

uno, *otros, cinco = numeros
print(uno, cinco, otros)  # 1 5 [2, 3, 4]
print('')

uno, dos, *otros, cuatro, cinco = numeros
print(dos, cuatro, otros)  # 2 4 [3]
print('')
