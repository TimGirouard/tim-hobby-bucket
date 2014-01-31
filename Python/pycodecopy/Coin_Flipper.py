#Guessing game reverse

print("Welcome to the guessing game.  Please pick a number between 1 and 100, and I will try to guess it.")
correct=0
guess=50
while correct==0:
    print("My guess is", str(guess)+".")
    yesno = input("Did I get it right? Please enter (Y/N):")
    print(yesno)
    if yesno==("y" or "Y"):
        correct+=1
        print("Hooray!  Maybe we can play again some time.")
    elif yesno==("n" or "N"):
        highlow = input("Aww, okay I'll try again.  Is it higher or lower (H/L)?")
        if highlow==("h" or "H"):
            guessinter = (guess + 100) // 2
            guess = (guess + guessinter) // 2
        elif highlow==("l" or "L"):
            guessinter = guess // 2
            guess = (guess + guessinter) // 2
        else:
            print ("Error, you need to type L or H.")
    else:
        print ("Error, you need to type Y or N.")
input("\n\nPlease press Enter to exit.")
