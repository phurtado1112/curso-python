""" implementa a clase Calculadora """


class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


a = float(input("Introduce un número: "))
b = float(input("Introduce otro número: "))

calc = Calculadora()

print("La suma es: ", calc.suma(a, b))
print("La resta es: ", calc.resta(a, b))
print("La multiplicación es: ", calc.multiplicacion(a, b))
print("La división es: ", calc.division(a, b))
