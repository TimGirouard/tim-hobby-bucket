#Guess my number game

import random

#Say Hello
print("Welcome to the Number Guessing Game.  My name is Robbie.")

print("I have chosen a number between 1 and 100.")

def ask_number(question, low, high, step=1):
    """Ask for a number within a range."""
    tries = 0
    response = None
    while response not in range(low, high+1):
        response = int(input(question))
    tries += step
    return response

#The Game
def main():
    import random
    tries=1
    guess = 0
    random = int(random.randint(1,100))
    while guess != random:
        guess = ask_number("What is your guess?", 1, 100)
        if guess>random:
            print("Lower...")
        if guess<random:
            print("Higher...")
        tries += 1
    print("\nYou got it! The number was", str(random) + ".")
    print("And it only took you", tries, "tries.")
    input("\n\nPress the enter key to exit.")

main()

#Victory!


