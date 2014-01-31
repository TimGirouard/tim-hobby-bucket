#Attribute Critter
#Demos creating and accessing object attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self,name):
        print("A new critter has been born!")
        self.name = name

    def __str__(self):
        rep += "name: " + self.name + "\n"

        return rep

    def talk(self):
        print("Hi. I'm", self.name, "\n")

#main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()
