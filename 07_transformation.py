name = "Nicolas"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("nicolas" + " molina")
print(10 + 20)
print("nicolas" + "12")

age = 12
print("mi edad es " + str(age))
print(f"mi edad es {age}")

age = input("escribe tu edad")     #aca ponemos que la edad sea igual al numero que se escriba
print(type(age)) #aca miramos que tipo queda la edad despues de lo anterior
age = int(age) #aca convertimos la edad de str a int (str es texto y int numeros)
age += 10 #aca sumamos el numero que pongan en la edad 
print(f"tu edad en 10 años sera {age}")