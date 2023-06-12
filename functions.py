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

# Contador de palabras: Cuenta la cantidad de palabras en una oración.

oracion = input("Ingrese una oración: ")
palabras = oracion.split()
cantidad_palabras = len(palabras)
print("Cantidad de palabras:", cantidad_palabras)

#Validador de contraseña: Solicita al usuario que ingrese una contraseña y verifica si cumple con ciertos criterios de seguridad (por ejemplo, longitud mínima, presencia de letras mayúsculas, números, etc.).

import re

def es_contraseña_segura(contraseña):
    longitud_minima = 8
    tiene_mayusculas = re.search(r"[A-Z]", contraseña)
    tiene_minusculas = re.search(r"[a-z]", contraseña)
    tiene_numeros = re.search(r"\d", contraseña)
    tiene_caracteres_especiales = re.search(r"\W", contraseña)

    if (
        len(contraseña) >= longitud_minima
        and tiene_mayusculas
        and tiene_minusculas
        and tiene_numeros
        and tiene_caracteres_especiales
    ):
        return True
    else:
        return False

contraseña = input("Ingrese una contraseña: ")

if es_contraseña_segura(contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña no cumple con los requisitos de seguridad.")

#Generador de números primos: Genera una lista de los primeros n números primos.

def generar_primos(n):
    primos = []
    num = 2
    while len(primos) < n:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primos.append(num)
        num += 1
    return primos

n = int(input("Ingrese la cantidad de números primos a generar: "))
primos_generados = generar_primos(n)
print("Números primos generados:", primos_generados)

# Multiplicación de todos los elementos en una lista:

nums = [1, 2, 3, 4, 5]

producto = functools.reduce(lambda x, y: x * y, nums)
print(producto)

# Filtrar palabras que comiencen con una letra específica:

palabras = ['manzana', 'banana', 'pera', 'naranja', 'sandía']
letra = 'b'

palabras_filtradas = list(filter(lambda x: x.startswith(letra), palabras))
print(palabras_filtradas)

# Obtener la longitud de cada palabra en una lista:

palabras = ['Hola', 'mundo', 'programación', 'funcional']

longitudes = list(map(lambda x: len(x), palabras))
print(longitudes)

# Generador de contraseñas:

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

