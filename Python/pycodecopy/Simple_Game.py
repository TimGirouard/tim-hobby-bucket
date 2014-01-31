# Simple Game
# Demos importing modules

import Games, random

print("Welcome to the world's simplest game!\n")

again = None
while again != "n":
    players = []
    num = Games.ask_number(question = "How many players? (2-5): ", low = 2,
                       high = 5)

    for i in range(num):
        name = input("Player name: ")
        score = random.randrange(100) + 1
        player = Games.Player(name, score)
        players.append(player)

    print("\nHere are the game results:")
    for player in players:
        print(player)

    again = Games.ask_yes_no("\nDo you want to play again? (y/n): ")

input("\n\nPress the enter key to exit.")
