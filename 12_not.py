#not
print(not True)
print(not False)

#not and
print("not and")
print("not True and True =>", not (True and True))
print("not True and False =>", not (True and False))
print("not False and True =>", not (False and True))
print("not False and False =>", not (False and False))

stock = input("ingrese el numero de stock =>") #creamos esto para que nos deje poner texto
stock = int(stock) #pasamos esto para que se convierta en sistema de numeros

print(not (stock >= 100 and stock <= 1000)) #aca como lo negamos estamos diciendo que tiene que ser fuera de 100 hasta el 1000
