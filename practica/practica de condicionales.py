
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("digite su edad =>"))

print(edad >= 18)

if edad >= 18:
    print("eres mayor de edad")

else:
    print("eres menor de edad")
"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
en la variable sin tener en cuenta mayúsculas y minúsculas."""

contraseña = "contraseña"
digite = input("digite su contraseña ")

if contraseña == digite.lower(): #el .lower es para que si o si se ponga en mayuscula
    print("acceso permitido")
else:
    print("acceso denegado")

""" Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el 
programa debe mostrar un error."""

print("Ingresa 2 numeros que quieras dividir")
numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2:"))
operacion = numero1 / numero2

print("su resultado es ", operacion)

if operacion == 0:
    print("ERROR")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
    
n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par") #n % 2: Esto calcula el residuo de la división de n entre 2. Si el residuo es 0, significa que n es divisible por 2, lo que indica que n es un número par.
else:
    print("El número " + str(n) + " es impar")