numbers =(1, 2, 3, 5)             #EN UNA TUPLA NO SE PUEDE AGREGAR NI MODIFICAR A COMPARACION DE LAS LISTAS
strings = ("nico", "zule", "santi", "nico")
print(numbers)
print("0 =>", numbers[0])
print("0 =>", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

print(numbers)
print(strings)
print(strings.index("zule"))
print(strings.index("nico"))

my_list = list(strings) #asi se cambia una tupla a una lista
print(my_list)
print(type(my_list))



