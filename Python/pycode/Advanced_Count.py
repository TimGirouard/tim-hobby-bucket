#Advanced Count

#Welcome the user

print("Welcome to the counting game, everybody's a winner!")

#Enter starting number

starting = int(input("\nPlease enter starting number: "))

#Enter ending number

ending = int(input("\nPlease enter ending number: "))

#Enter count interval

interval = int(input("\nPlease enter the number to count by: "))

#Display counting output

print("\nHow do I love thee?\n\nLet me count the ways...")

for i in range(starting, ending+1, interval):
    print(i, end=" ")

input("\n\nYou win again!\n\nPress the enter key to exit.\n")

