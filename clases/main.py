import random

options = ("piedra", "papel", "tijera")

user_option = input("piedra, papel o tijera: ").lower()

if not user_option in options:
    print("esa opcion no es valida")

computer = random.choice(options)

print("user option => ", user_option)
print("com´puter option =>", computer)

if user_option == computer:
    print("Empate")

elif user_option == "piedra":
    if computer == "tijera":
        print("piedra gana a tijera")
        print("user gana")
    else:
        print("papel gana a piedra")
        print("user gana")
elif user_option == "papel":
    if computer == "piedra":
        print("papel gana a tijera")
        print("user gano")
    else:
        print("tijera gana a papel")
        print("computer gana")
elif user_option == "tijera":
    if computer == "papel":
        print("tijera gana a papel")
        print("user gana")
    else:
        print("peidra gana a tijera")
        print("computer gana")