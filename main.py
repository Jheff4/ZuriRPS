import random
from time import sleep

print("Rock", end="\r")
sleep(2)

print("Paper", end="\r")
sleep(2)

print("Scissors", end="\r")
sleep(2)


print("Hello, let's play 'Rock Paper Scissors'")
sleep(4)

game_list = ["R", "P", "S"]
random_letter = random.choice(game_list)
#print(random_letter)

first = "Rock"
second = "Paper"
third = "Scissors"

for i in range(100):
    game = input("Pick 'R', 'P' or 'S': ")
    game = game.upper()

    if game not in game_list:
        print("Error")
        continue

    elif game == "R" and random_letter == "S":
        print("Player Wins")
        print("Player: (Rock) : CPU (Scissors)")
        break

    elif random_letter == "R" and game == "S":
        print("CPU Wins")
        print("Player: (Scissors) : CPU (Rock)")
        break

    elif game == "P" and random_letter == "R":
        print("Player Wins")
        print("Player: (Paper) : CPU (Rock)")
        break

    elif random_letter == "P" and game == "R":
        print("CPU Wins")
        print("Player: (Rock) : CPU (Paper)")
        break

    elif game == "S" and random_letter == "P":
        print("Player Wins")
        print("Player: (Scissors) : CPU (Paper)")
        break

    elif random_letter == "S" and game == "P":
        print("CPU Wins")
        print("Player: (Paper) : CPU (Scissors)")
        break

    elif game == random_letter:
        print("Tie")

        if game == "R" and random_letter == "R":
            print("Player: (" + first + ") : CPU (" + first + ")")
            continue

        elif game == "P" and random_letter == "P":
            print("Player: (" + second + ") : CPU (" + second + ")")
            continue

        elif game == "S" and random_letter == "S":
            print("Player: (" + third + ") : CPU (" + third + ")")
            continue


    else:
        print("Player: (" + game + ") : CPU (" + random_letter + ")")
