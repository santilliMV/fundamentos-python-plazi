"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla."""

"""asignaturas = ["Matemáticas, Física, Química, Historia y Lengua"]

print(asignaturas)"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por 
pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista."""

"""asignaturas = ["Matemáticas, Física, Química, Historia y Lengua"]

for i in asignaturas:
    print("yo estudio", i)"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario 
la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las 
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""

"""subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de 
menor a mayor."""

"""lista = []

for i in range(6):
    lista.append(int(input("Digite los numeros ganadores de la lotereia ")))
lista.sort()
print("los numeros ganadores son: ", lista)"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""

"""numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.reverse()
for i in numeros:
    print(i, end=", ")"""

 #//////////////////////////////////////////////////////////

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
asignaturas que el usuario tiene que repetir."""

"""subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))"""

 #//////////////////////////////////////////////////////////

"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la 
lista resultante."""

"""abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in abc[2: 29: 3]:
    abc.remove(i)
print(abc)"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

"""palabra = input("EScriba una palabra para saber si es palindroma o no ")

if palabra == palabra[::-1]:
    print("es palindroma")
else:
    print("no es palindroma")"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

"""palabra = input("EScriba una palabra: ")
vocales = ["a", "e", "i", "o", "u"]

print(palabra)

for i in vocales:
    
    print(f" {i} = {palabra.count(i)}", end=" ")"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el
menor y el mayor de los precios."""

"""precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort()
print(f"el menor es {precios[0]} y el mayor es {precios[-1]}")"""

#//////////////////////////////////////////////////////////

"""Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista 
y muestre por pantalla su media y desviación típica."""


