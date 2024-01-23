#and
print("and")
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input("ingrese el numero de stock =>") #creamos esto para que nos deje poner texto
stock = int(stock) #pasamos esto para que se convierta en sistema de numeros

print(stock >= 100 and stock <= 1000) #aca estamos diciendo que el valor tiene q estar entre 100 o 100 para que sea verdadero

#or
print("or")
print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)

role = input("digita el rol => ")

print(role == "admin" or role == "seller") #aca le estoy diciendo que si es admin o seller es true de lo contrario es false
