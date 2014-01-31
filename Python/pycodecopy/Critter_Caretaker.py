#Critter Caretaker
#A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str(self):
        print("Hunger is", self.hunger, "and boredom is", self.boredom, "now.\n")
        self.__pass_time()
              
    def publicstr(self):
        self.__str()
              
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food):
        print("Burp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("What do you want to name your critter?:")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice:")
        print()

        # exit
        if choice == "0":
            print("Thank you for playing.  Good-bye.")

        #listen to your critter
        elif choice == "1":
            crit.talk()

        #feed your critter
        elif choice == "2":
            foodness = 0
            while foodness not in [1,2,3,4]:
                foodstring = input("How many kibbles do you want to feed me? (1-4)")
                if foodstring in ["1","2","3","4"]:
                    foodness = int(foodstring)
                else:
                    print("That is not a valid number of kibbles.")  
            crit.eat(foodness)

        #play with your critter
        elif choice == "3":
            playtime = 0
            while playtime not in [1,2,3,4]:
                playstring = input("How many minutes do you want to play for? (1-4)")
                if playstring in ["1","2","3","4"]:
                    playtime = int(playstring)
                else:
                    print("That is not a valid number of minutes.")
            crit.play(playtime)

        #shhh secret choice
        elif choice == "4":
              crit.publicstr()

        #any other choice
        else:
            print("\nSorry, but", choice, "is not a valid selection.")

main()
("\n\nPress the enter key to exit.")
