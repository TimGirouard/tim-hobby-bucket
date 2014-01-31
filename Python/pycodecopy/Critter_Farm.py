#Critter Farm
#Tons of virtual pets to care for

class Critter(object):
    """A virtual pet"""
    rainbows_total = 0

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self, times=1):
        self.hunger += 1*times
        self.boredom += 1*times

    def __str(self):
        print("Hunger for", self.name, "is", self.hunger, "and boredom is", self.boredom, "now.\n")
              
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

    def eat(self, food):
        print("Burp.  Thank you.")
        self.__pass_time()
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
            
    def play(self, fun):
        print("Wheee!")
        if fun == 1:
            self.__pass_time(.25)
        if fun == 2:
            self.__pass_time(.5)
        if fun == 3:
            self.__pass_time(.75)
        if fun == 4:
            self.__pass_time(1)
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0

    def public_pass_time(self):
        self.__pass_time()

    def collectrainbows(self):
        rainbows = 0
        if self.mood == "happy":
            rainbows += 3
        if self.mood == "okay":
            rainbows += 1
        if self.mood == "frustrated":
            rainbows -= 1
        if self.mood == "mad":
            rainbows -= 3
        self.__pass_time()
        return rainbows

def main():
    critlist = []
    rainbows_total = 10
    crit_name = input("What do you want to name your first critter?:")
    critlist.append(Critter(crit_name))
    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Check on your critter farm
        2 - Feed your critters (1/4 rainbow)
        3 - Play with your critters
        4 - Buy a new critter (10 rainbows)
        5 - Collect rainbows
        """)

        choice = input("Choice:")
        print()

        # exit
        if choice == "0":
            print("Thank you for playing.  Good-bye.")

        #listen to your critter
        elif choice == "1":
            print("You have", rainbows_total, "rainbows available.\n")
            for crit in critlist:
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
            for crit in critlist:
                crit.eat(foodness)
                rainbows_total -= foodness*.25

        #play with your critter
        elif choice == "3":
            playtime = 0
            while playtime not in [1,2,3,4]:
                playstring = input("How many minutes do you want to play for? (1-4)")
                if playstring in ["1","2","3","4"]:
                    playtime = int(playstring)
                else:
                    print("That is not a valid number of minutes.")
            for crit in critlist:
                crit.play(playtime)

        #add a new critter
        elif choice == "4":
            if rainbows_total >= 10:
                for crit in critlist:
                    crit.public_pass_time()
                crit_name = input("What do you want to name your next critter?:")
                rainbows_total -= 10
                critlist.append(Critter(crit_name))
            else:
                print("You don't have enough money for that!")

        #collect points
        elif choice == "5":
            for crit in critlist:
                rainbows_total += crit.collectrainbows()
            print("You have", rainbows_total, "rainbows available.\n")
            for crit in critlist:
                crit.talk()
            
        #shhh secret choice
        elif choice == "6":
            for crit in critlist:
                crit.publicstr()

        #any other choice
        else:
            print("\nSorry, but", choice, "is not a valid selection.")

main()
("\n\nPress the enter key to exit.")
