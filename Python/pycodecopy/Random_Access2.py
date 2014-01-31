# Random Access
# Demonstrates string indexing

import random

word = "index"
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(5):
    print(word[i])

input("\n\nPress the enter key to exit.")
