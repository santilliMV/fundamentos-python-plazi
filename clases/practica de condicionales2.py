"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que 
tributar o no."""

nombre = input("cual el su nombre: ")
edad = int(input("cual es su edad: "))
ingresos = int(input("ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    print(nombre, "tienes que tributar por tener", edad, "y por tener", ingresos, "de ingresos")
else:
    print(nombre, "no tienes que tributar por tener", edad, "y por tener", ingresos, "de ingresos")

"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que 
le corresponde."""

nombre = input("cual es tu nombre: ")
sexo = input("eres M o H ")

if (sexo == "M" and nombre.lower() <= "m") or (sexo == "H" and nombre.lower() <= "n"):
    print(nombre, "eres del grupo A")
else:
    print(nombre, "eres del grupo B")