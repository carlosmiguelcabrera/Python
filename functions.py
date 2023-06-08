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

# Ejercicio 4: Invertir una cadena de texto

cadena = "Hola, mundo!"
inversa = cadena[::-1]
print("La cadena invertida es:", inversa)

# Ejercicio 5: Calcular el área de un círculo

import math

radio = 5
area = math.pi * radio**2
print("El área del círculo es:", area)

# Generador de números pares: Genera una lista de números pares en un rango dado.

inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))

numeros_pares = [num for num in range(inicio, fin + 1) if num % 2 == 0]
print("Números pares:", numeros_pares)


# Conversor de Celsius a Fahrenheit: Convierte una temperatura en grados Celsius a grados Fahrenheit.

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("La temperatura en grados Fahrenheit es:", fahrenheit)

# Verificador de palíndromos: Verifica si una palabra o frase es un palíndromo.

def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

palabra = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

# Calculadora de promedio: Solicita al usuario una lista de números y calcula el promedio.

n = int(input("Ingrese la cantidad de números: "))
numeros = []
for i in range(n):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)


#Números primos: Muestra todos los números primos en un rango dado.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))

print("Números primos:")
for num in range(inicio, fin + 1):
    if es_primo(num):
        print(num)
