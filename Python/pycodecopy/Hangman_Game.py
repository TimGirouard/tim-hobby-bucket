#Hangman Game

#Explain the game

# The classic game of Hangman. The computer picks a random word
# and the player wrong to guess it, one letter at a time. If the player
# can't guess the word in time, the little stick figure gets hanged.

#imports
import random

# constants
HANGMAN = (
"""
 ------
 |     |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |     |
 |     0
 |

  |
  |
  |
  |
  |
----------
""",
"""
 ------
 |     |
 |     0
 |    -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |     |
 |     0
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |     |
 |     0
 |  /-+-/
 |
 |
 |

  |
  |
----------
""",
"""
 ------
 |     |
 |     0
 |  /-+-/
 |     |
 |
 |
 |
 |
----------
""",
"""
 ------
 |     |
 |     0
 |  /-+-/
 |     |
 |     |
 |    |
 |    |
 |
----------
""",
"""
 ------
 |     |
 |     0
 |  /-+-/
 |     |
 |     |
 |    | |
 |    | |
 |
----------
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("WORDS" "PALEONTOLOGIST", "FALLACY", "PANCAKES", "STIPEND", "TRICERATOPS")

#Initialize Variables

word = random.choice(WORDS) #the word to be guessed

so_far = "_" * len(word) # one dash for each letter in word to be guessed

wrong = 0  # number of wrong guesses player has made

used = [] #set of letters already guessed

print("Welcome to Hangman.  Guess away!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("You've used the following letters so far:\n", used)
    print("\nSo far the word is:\n", so_far)

    guess = input("Enter your guess: ")
    while len(guess) != 1:
        guess = input("Please enter a single character:\n")

    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("Yes!", guess, "is in the word!")

        #create a new so_far to include guess

        new = ""

        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("Sorry,", guess, "is not in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("Sorry, you didn't guess it.\nYou've been hanged.")
else:
    print("You guessed it!")

print("The word was", word)
    
input("\n\nPress the enter key to exit.")


