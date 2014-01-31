# Who's Your Daddy
# Demonstrates using complex dictionaries

yourdaddy = {"Emilio Esteves": "Martin Sheen",
        "Tim Girouard": "Peter Girouard",
        "Isaac" : "Abraham",
        "George W Bush" : "George HW Bush",
        "Martin Sheen" : "Francisco Estévez Martinez",
        "Peter Girouard" : "Hector Girouard",
        "Abraham" : "Terah",
        "George HW Bush" : "Prescott Sheldon Bush"}
choice = None
while choice != "0":

    print(
    """
    Geek Translator

    0 - Quit
    1 - Who's your daddy?
    2 - Who's your granddaddy?
    3 - Add a father-son pair
    4 - Correct a father-son pair
    5 - Delete a father-son pair
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # get a daddy
    elif choice == "1":
        for baby in yourdaddy:
            print(baby)
        baby = input("Who's the baby?: ")
        if baby in yourdaddy:
            daddy = yourdaddy[baby]
            print("\n", baby, "has a great dad, and his name is", daddy)
        else:
            print("\nSorry, I don't know", baby)

    # get a granddaddy
    elif choice == "2":
        for baby in yourdaddy:
            print(baby)
        baby = input("Who's the baby?: ")
        if baby in yourdaddy:
            daddy = yourdaddy[baby]
            if daddy in yourdaddy:
                granddaddy = yourdaddy[daddy]
                print("\n", baby, "has a great granddad, and his name is",
                      granddaddy)
            else:
                print("\nSorry, I don't know the granddaddy of", baby,
                      "\n\nBut his dad is", daddy,
                      "\n\nMaybe you can give his daddy a daddy.",
                      "Try adding this pair to the list.")
        else:
            print("\nSorry, I don't know", baby)
            
    # add a baby-daddy pair
    elif choice == "3":
        baby = input("What baby do you want me to add?: ")
        if baby not in yourdaddy:
            daddy = input("\nWho's the daddy?: ")
            yourdaddy[baby] = daddy
            print("\n", baby, "has been added.")
        else:
            print("\nThat babydaddy already exists!  Try redefining it.")

    # redefine an existing baby
    elif choice == "4":
        baby = input("What baby do you want me to redaddy?: ")
        if baby in yourdaddy:
            daddy = input("Who's the new daddy?: ")
            yourdaddy[baby] = daddy
            print("\n", baby, "has been redaddied.")
        else:
             print("\nThat baby doesn't exist!  Try adding it.")

    # delete a term-definition pair
    elif choice == "5":
        baby = input("What baby do you want me to delete?: ")
        if baby in yourdaddy:
            del yourdaddy[baby]
            print("\nOkay, I deleted", baby)
        else:
            print("\nI can't do that!", baby, "doesn't exist in the list.")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
