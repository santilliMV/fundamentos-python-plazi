"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""
"""palabra = input("digite una palabra: ")

for i in range(10):
    print(palabra)"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

"""edad = int(input("digite su edad: "))

for i in range(edad):
    print("haz cumplido", str(i+1), "años")"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

"""numero = int(input("Digite un numero positivo: "))

for i in range(1, numero+1, 2):
    print(i, end=", ")"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

"""numero = int(input("idigte un numero para hacerle cuanta hasta 0: "))

for i in range(numero, -1, -1):
    print(i, end=", ")"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido 
en la inversión cada año que dura la inversión."""

"""amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido."""

"""numero = int(input("cuantos pisos de asterioscos quiere: "))

for i in range(numero):
    print("*" * (1+i))"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

"""for i in range(1, 11):
        print(f"tabla del 1: 1x{i}= {1 * i}")
        print(f"tabla del 2: 2x{i}= {2 * i}")
        print(f"tabla del 3: 3x{i}= {3 * i}")
        print(f"tabla del 4: 4x{i}= {4 * i}")
        print(f"tabla del 5: 5x{i}= {5 * i}")
        print(f"tabla del 6: 6x{i}= {6 * i}")
        print(f"tabla del 7: 7x{i}= {7 * i}")
        print(f"tabla del 8: 8x{i}= {8 * i}")
        print(f"tabla del 9: 9x{i}= {9 * i}")
        print(f"tabla del 10: 10x{i}= {10 * i}")"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo."""

"""n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la 
contraseña correcta."""

"""contraseña = "hola"

while True:
    digitar = input("como es su contraseña: ")
    if contraseña == digitar:
        print ("correcto")
        break
    else: 
        print("intente de nuevo")"""
    
#////////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

"""n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última."""

"""palabra = input("digite una palabra ")

palabra = palabra[::-1]

for i in palabra:
    print(i, end=(" "))"""

#////////////////////////////////////////////////////////////

"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."""

"""frase = input("digite una frase ")
letra = input("digite una letra")

numero = int(frase.count(letra))

for i in range(1, numero):
    print((i) * letra, end=("/n"))"""

#////////////////////////////////////////////////////////////

"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""


while True:
    cosas = input("para salir pon salir ")
    if cosas == "salir":
        break