# Menu
# Lets you mix-and-match your own meal

from tkinter import *

class Application(Frame):
    """ A GUI application for a favorite movie type. """

    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets for movie type choices. """
        # create description label
        Label(self, text = "Choose your burger type"
              ).grid(row=0,column=0,sticky=W)
        
        # create instruction label
        Label(self,text="Select one:").grid(row=1,column=0,sticky=W)

        # create variable for burger
        #self.burger = StringVar()
        #self.burger.set(None)

        # create variable for side
        self.side = StringVar()
        self.side.set(None)

        # create Chicken radio button
        self.wants_chicken = BooleanVar()
        Checkbutton(self,text="Chicken ($6)",variable=self.wants_chicken,
                    command=self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        # create Beef radio button
        self.wants_beef = BooleanVar()
        Checkbutton(self,text="Beef ($5)",variable=self.wants_beef,
                    command=self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        # create Veggie radio button
        self.wants_veggie = BooleanVar()
        Checkbutton(self,text="Veggie ($4)",variable=self.wants_veggie,
                    command=self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        # create description label
        Label(self, text = "Choose your side"
              ).grid(row=0,column=2,sticky=W)
        
        # create instruction label
        Label(self,text="Select one:").grid(row=1,column=2,sticky=W)

        # create fries radio button
        Radiobutton(self,text="Fries",variable=self.side,
                    value="fries.",command=self.update_text
                    ).grid(row = 2, column = 2, sticky = W)

        # create mashed potatoes radio button
        Radiobutton(self,text="Mashed Potatoes",variable=self.side,
                    value="mashed potatoes.",command=self.update_text
                    ).grid(row = 3, column = 2, sticky = W)

        # create salad radio button
        Radiobutton(self,text="Salad",variable=self.side,
                    value="salad.",command=self.update_text
                    ).grid(row = 4, column = 2, sticky = W)

        # create description label
        Label(self, text = "Any toppings?"
              ).grid(row=0,column=4,sticky=W)
        
        # create instruction label
        Label(self,text="Choose from the list:").grid(row=1,column=4,sticky=W)

        # create bacon check button
        self.wants_bacon = BooleanVar()
        Checkbutton(self,text="Bacon ($1)",variable=self.wants_bacon,
                    command=self.update_text
                    ).grid(row = 2, column = 4, sticky = W)

        # create cheese check button
        self.wants_cheese = BooleanVar()
        Checkbutton(self,text="Cheese ($0.50)",variable=self.wants_cheese,
                    command=self.update_text
                    ).grid(row = 3, column = 4, sticky = W)

        # create avocado check button
        self.wants_avocado = BooleanVar()
        Checkbutton(self,text="Avocado ($0.50)",variable=self.wants_avocado,
                    command=self.update_text
                    ).grid(row = 4, column = 4, sticky = W)

        # create lettuce check button
        self.wants_lettuce = BooleanVar()
        Checkbutton(self,text="Lettuce (free)",variable=self.wants_lettuce,
                    command=self.update_text
                    ).grid(row = 2, column = 5, sticky = W)

        # create tomato check button
        self.wants_tomato = BooleanVar()
        Checkbutton(self,text="Tomato (free)",variable=self.wants_tomato,
                    command=self.update_text
                    ).grid(row = 3, column = 5, sticky = W)

        # create onion check button
        self.wants_onion = BooleanVar()
        Checkbutton(self,text="Onion (free)",variable=self.wants_onion,
                    command=self.update_text
                    ).grid(row = 4, column = 5, sticky = W)
        
        # create text widget to display message
        self.results_txt = Text(self, width = 50, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 6)

    def update_text(self):
        """ Update text widget and display user's favorite movie type. """
        price = 0.00
        message = "You chose "
        if self.wants_chicken.get():
            message+="a chicken burger"
            price += 5
        elif self.wants_beef.get():
            message+="a beef burger"
            price += 4
        elif self.wants_veggie.get():
            message+="a veggie burger"
            price += 3
        else:
            message+="no burger"
        message += " with "
        notoppings = 0
        if self.wants_bacon.get():
            message += "bacon, "
            price += 1
            notoppings +=1
        if self.wants_cheese.get():
            message += "cheese, "
            price += .50
            notoppings +=1
        if self.wants_avocado.get():
            message += "avocado, "
            price += .50
            notoppings +=1
        if self.wants_lettuce.get():
            message += "lettuce, "
            notoppings +=1
        if self.wants_tomato.get():
            message += "tomato, "
            notoppings +=1
        if self.wants_onion.get():
            message += "onion, "
            notoppings +=1
        if notoppings == 0:
            message += "no toppings, "
        message += "and "
        if "None" in self.side.get():
            message += "no side."
        else:
            message += "a side of " + self.side.get()
            price += 1
        message += " And your total is $"+str(price)+"0."

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

# main
root = Tk()
root.title("Restaurant Menu")
#root.geometry("300x150")

# create a frame in the window to hold other widgets
app = Application(root)

#kick off the window's event loop
root.mainloop()
