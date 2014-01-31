#Print a random word list

#Imports

import random

#Welcome to the program

print("Welcome to the random word generator.\n\n")
print("Please enter five words (any characters allowed)...\n")

#Set a list

words = ["string"]*5

#Fill the list

i=0

while i<5:
    print("\nWord", i+1)
    word = input(": ")
    if len(word) == 0:
        print("Please enter a word (no blanks).")
    elif len(word) != 0:
        words[i] = word
        i += 1
    else:
        print("Oh no, you broke the program!")

#Produce Output

print("\nYour word list is:\n")
print(words)
print("\nLet me just put those all in a hat, and...voila!  Your word is:", random.choice(words))

#Exit the program
input("\nPress any key to exit.\n")
