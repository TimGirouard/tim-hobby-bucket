# Word Guess
#
# The computer picks a random word and then the player has to guess it

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct

correct = word
score = 10
tries = 1

# start the game
print(
"""

           Welcome to Word Guesser!

   Can you guess what word I'm thinking of?
If you get it on the first try, you get 10 points!
 (Press the enter key at the prompt to quit.)
"""

)

print("There are", len(word), "letters in the word.")

guess = input("\nYour guess: ")

while guess != correct and guess != "":
    score -= 2
    tries +=1
    print("\nTry again please.")
    letter=input("\nWhat letter do you think is in the word? ")
    while len(letter) != 1:
        print("\nPlease enter one letter at a time.")
        letter=input("\nWhat letter do you think is in the word? ")
    if letter.lower() in word:
        print("\nYes, that letter is in the word!")
    else:
        print("\nSorry, that letter is not in the word.")
    guess = input("\nYour guess: ")

        
if guess == correct:
    print("\nThat's it! You guessed it!\n")

    print("Your score is", score, "because you guessed it in", tries, "tries. Thanks for playing.")

input("\n\nPress the enter key to exit.")
