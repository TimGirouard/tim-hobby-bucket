#Character Creator

#Initialize Attributes

strength = 0
health = 0
wisdom = 0
dexterity = 0
pool = 30
done = 0
#Welcome to the creator

print("Welcome to the character creator.\n\n")

while done!=1:

#Reinitialize pool    
    pool = 30

#Initialize attributes
    print("Your attributes are:\n\nStrength =",strength,"\nHealth =",
          health, "\nWisdom =", wisdom, "\nDexterity =", dexterity)
    print("\nPlease input initial values.\n\n")
    try:
        strength = int(input("\nStrength: \n"))
    except ValueError:
        print("\nPut in a number, dude.\n")
        print("\nI think you meant to say 5.\n")
        strength = 5
    pool -= strength
    try:
        health = int(input("\nHealth: \n"))
    except ValueError:
        print("\nPut in a number, dude.\n")
        print("\nI think you meant to say 5.\n")
        health = 5
    pool -= health
    try:
        wisdom = int(input("\nWisdom: \n"))
    except ValueError:
        print("\nPut in a number, dude.\n")
        print("\nI think you meant to say 5.\n")
        wisdom = 5
    pool -= wisdom
    try:
        dexterity = int(input("\nDexterity: \n"))
    except ValueError:
        print("\nPut in a number, dude.\n")
        print("\nI think you meant to say 5.\n")
        strength = 5
    pool -= dexterity

#Test for value validity
    if pool < 0:
        print("\nYou do not have enough points for that.  Please try again.\n")
        strength = 0
        health = 0
        wisdom = 0
        dexterity = 0
    elif pool > 0:
        print("\nYou still have points left.  Are you sure about these values?\n")
    else:
        print("\nExcellent choice!\n")
    yesno = "k"
    while yesno.lower() != "y" and yesno.lower() !="n":
        yesno = input("\nWould you like to try again [y/n]?\n")
        if yesno.lower() == "y":
            done = 0
        elif yesno.lower() == "n":
            done = 1
            print("Your final attributes are:\n\nStrength =",strength,"\nHealth =",
          health, "\nWisdom =", wisdom, "\nDexterity =", dexterity)
        else:
            print("\nPlease input y or n.\n")
#Exit the program
input("\nPress any key to exit.\n")
