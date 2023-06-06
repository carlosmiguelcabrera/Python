# Ejercicio 1: Suma de dos números

num1 = 10
num2 = 5
suma = num1 + num2
print("La suma es:", suma)

# Ejercicio 2: Factorial de un número

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = 5
resultado = factorial(numero)
print("El factorial de", numero, "es", resultado)


