"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""

renta = int(input("Cual es su renta: "))

if renta < 10000:
    print("tienes que pagar 5%")

elif renta >= 10000 and renta < 20000:
    print("tienes que pagar 15% que es ", (renta * 15)/ 100, "$")

elif renta >= 20000 and renta < 35000:
    print("tienes que pagar el 20% que es", (renta * 20)/ 100, "$")

elif renta >= 35000 and renta < 60000:
    print("tienes que pagar el 30% que es", (renta * 30)/ 100, "$")

elif renta >= 60000:
    print("tienes que pagar 45% que es", (renta * 45)/ 100, "$")

"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación 
comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada 
nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que 
recibirá el usuario."""

puntos = float(input("Digite los puntos: "))

if puntos == 0.0:
    print("Inaceptable")

elif puntos == 0.4:
    print("aceptable")

elif puntos >= 0.6:
    print("meritorio")

else:
    print("digito invalido")

"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática 
el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio 
de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 
10€."""

edad = int(input("digite sue edad: "))

if edad < 4:
    print("puede entrar gratis")

if edad >= 4 and edad < 18:
    print("tiene que pagar 5$")

if edad > 18:
    print("tiene que pagar 10$")

"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza 
aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú 
con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están 
en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

tipo = input("quiere pizza vegetariana?: ")

if tipo.lower() == "si":
    vegetariana = input("Eliga pimiento o tofu: ")

    if vegetariana.lower() == "pimiento":
        print("su pizza es vegetariana y lleva tofu, mozzarella y tomate")

    elif vegetariana.lower() == "tofu":
        print("su pizza es vegetariana y lleva tofu, mozzarella y tomate")

if tipo.lower() == "no":
    novegetariana = input("Eliga peperoni, jamon, o salmon ")

    if novegetariana.lower() == "peperoni":
        print("su pizza no es vegetariana y lleva peperoni, mozzarella y tomate")

    elif novegetariana.lower() == "jamon":
        print("su pizza no es vegetariana y lleva jamon, mozzarella y tomate")
    
    elif novegetariana.lower() == "salmon":
        print("su pizza no es vegetariana y lleva salmon, mozzarella y tomate")

else:
    print("vuelva a intentar")

              
              
            