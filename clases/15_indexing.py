text = "ella sabe python"
print(text[0]) #sirve para poner un caracter espcifico depende de la ubicacion 
print(text[1])

size = len(text)
print(size)
print(text[size - 1])
print(text[-1])

#slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:]) #sirve q vaya desde ese punto hasta el final
print(text[:])
print(text[10:16:1])
print(text[10:16:2])#sirve para hacer saltos de letra
print(text[::2])