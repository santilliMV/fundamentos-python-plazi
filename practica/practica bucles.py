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

numero = int(input("Digite un numero positivo: "))

for i in range(1, numero+1, 2):
    print(i, end=", ")