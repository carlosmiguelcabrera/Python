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

# Ejercicio 3: Verificar si un número es primo

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            return False
    return True

num = 17
if es_primo(num):
    print(num, "es un número primo")
else:
    print(num, "no es un número primo")


