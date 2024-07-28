''' Calculadora básica '''
print("Bienvenido a la Calculadora básica")
print('Para salir, escriba "exit"')
print("Operaciones disponibles: suma (sum), resta (res), multiplicación (mul), división (div)")

resultado = ''

while True:
    if not resultado:
        num1 = float(input("Ingrese el primer número: "))
        if resultado.lower() == "exit":
            break
        num1 = float(num1)
    operacion = input("Ingrese la operación a realizar: ")
    if operacion.lower() == "exit":
        break

    if operacion not in ["sum", "res", "mul", "div"]:
        print("Operación no válida")
        continue

    num2 = float(input("Ingrese el segundo número: "))
    if operacion == "sum":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "res":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "mul":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "div":
        if num2 == 0:
            print("No se puede dividir por cero")
        else:
            print(f"Resultado: {num1 / num2}")
