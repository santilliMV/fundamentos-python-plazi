import random

options = ("piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0
rounds = 1

while True:

    print("*" * 10)
    print("Ronda", rounds)
    print("*" * 10)

    print("victorias de el computador", computer_wins)
    print("victorias de el usuario", user_wins)



    user_option = input("piedra, papel o tijera: ").lower()

    if not user_option in options:
        print("esa opcion no es valida")
        continue    

    computer = random.choice(options)

    print("user option => ", user_option)
    print("computer option =>", computer)

    if user_option == computer:
        print("Empate")

    elif user_option == "piedra":
        if computer == "tijera":
            print("piedra gana a tijera")
            print("user gana")
            user_wins +=1
        else:
            print("papel gana a piedra")
            print("computer gana")
            computer_wins += 1
    elif user_option == "papel":
        if computer == "piedra":
            print("papel gana a tijera")
            print("user gano")
            user_wins +=1
        else:
            print("tijera gana a papel")
            print("computer gana")
            computer_wins += 1
    elif user_option == "tijera":
        if computer == "papel":
            print("tijera gana a papel")
            print("user gana")
            user_wins +=1
        else:
            print("peidra gana a tijera")
            print("computer gana")
            computer_wins += 1

    if computer_wins == 2:
        print("el ganador es la computadora")
        break

    if user_wins == 2:
        print("el ganador es la usuario")
        break

    rounds += 1