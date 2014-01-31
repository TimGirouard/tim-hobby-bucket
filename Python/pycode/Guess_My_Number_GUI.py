#Guess my number game with GUI

from tkinter import *

class Application(Frame):
    """ A GUI application for a favorite movie type. """
    import random
    def __init__(self, master, guesses=0, randomnum = int(random.randint(1,100))):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.guesses = guesses
        self.randomnum = randomnum

    def create_widgets(self):
        """ Create widgets for movie type choices. """
        #set random number
        # create description label
        Label(self, text = "Number Guessing Game"
              ).grid(row=0,column=0,sticky=W)
        
        # create instruction label
        Label(self,text="I have chosen a number between 1 and 100.\n" \
              "What is your guess?").grid(row=1,column=0,sticky=W)

        # create variable for single favorite type of movie
        #self.number = StringVar()
        #self.number.set(None)

        # set entry for number
        self.number_ent = Entry(self)
        self.number_ent.grid(row=1,column=1,sticky=W)
        # create submit button
        #self.submit_bttn = Button(self, text = "Submit", command = lambda: self.reveal(numnum))
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

        # create text widget to display message
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def reveal(self):
        """ Display message based on guess. """
        import random
        randomnum = self.randomnum
        contents = int(self.number_ent.get())
        if contents == randomnum:
            self.guesses += 1
            message = "You got it! And it only took "+str(self.guesses)+" guesses!"
            self.guesses = 0
            self.randomnum = int(random.randint(1,100))
        elif contents < randomnum:
            message = "A little higher..."
            self.guesses += 1
        elif contents > randomnum:
            message = "A little lower..."
            self.guesses += 1
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

"""
def ask_number(question, low, high, step=1):
    "Ask for a number within a range."
    tries = 0
    response = None
    while response not in range(low, high+1):
        response = int(input(question))
    tries += step
    return response

#The Game
def main():
    import random
    tries=1
    guess = 0
    random = int(random.randint(1,100))
    while guess != random:
        guess = ask_number("What is your guess?", 1, 100)
        if guess>random:
            print("Lower...")
        if guess<random:
            print("Higher...")
        tries += 1
    print("\nYou got it! The number was", str(random) + ".")
    print("And it only took you", tries, "tries.")
    input("\n\nPress the enter key to exit.")

main()

#Victory!
"""




# main
root = Tk()
root.title("Movie Chooser 2")
#root.geometry("300x150")

# create a frame in the window to hold other widgets
app = Application(root)

#kick off the window's event loop
root.mainloop()

