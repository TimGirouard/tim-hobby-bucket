#Backwards Printer

#Welcome the user

print("Welcome to the backwards printer, where backward is the way forward!")

#Enter string

initial = input("\nPlease enter initial word: ")

#Reverse the word

position = len(initial)
backwards = ""

while initial:
    
    backwards += initial[position-1]
    position -= 1
    initial = initial[:position]

#Display backwards output

print("\nI think that looks better this way...\n\n")

print(backwards)

input("\n\nBetter, right?\n\nPress the enter key to exit.\n")

