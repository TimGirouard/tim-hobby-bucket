# Word Jumble Improved
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct

correct = word
hint = word
score = 10

# create a jumbled version of the word
jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""

           Welcome to Word Jumble!

   Unscramble the letters to make a word.
 (Press the enter key at the prompt to quit.)
"""

)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    score -= 2
    print("\nTry again please.")
    yesno=input("\nWould you like a hint? (Y/N): ")
    if yesno.lower() == "y":
        jumble2 = ""
        hinttemp = hint
        while hinttemp:
            position = random.randrange(len(hinttemp))
            jumble2 += hinttemp[position]
            hinttemp = hinttemp[:position] + hinttemp[(position + 1):]
        print("\nYour hint is:", jumble2)
        score -= 1
    elif yesno.lower() == "n":
        guess = input("\nYour guess: ")
    else:
        print("Please enter Y or N.")

if guess == correct:
    print("That's it! You guessed it!\n")

    print("Your score is", score, ". Thanks for playing.")

input("\n\nPress the enter key to exit.")
