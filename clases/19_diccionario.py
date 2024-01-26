my_dict = {}
print(type(my_dict))

my_dict = {
    "avion": "fiuuuuuuuun",
    "name": "nicolas",
    "last_name": "molina monrroy",
    "age": 87
}
print(my_dict)
print(len(my_dict))

print(my_dict["age"])
print(my_dict["last_name"])
print(my_dict.get("unvalor")) #esta es la q se debe usar para buscar algo dentro del dicionario

print("avion" in my_dict)
print("otroqueno" in my_dict)