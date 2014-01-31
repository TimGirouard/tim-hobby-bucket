# Mad Lib 2
# Creates a story based on user input

from tkinter import *

class Application(Frame):
    """ A GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and display it. """
        
        # create instruction label
        Label(self,text="Enter information for a new story..."
              ).grid(row=0,column=0,columnspan=2,sticky=W)

        # create a label and text entry for the name of a person
        Label(self,text="Person 1: "
              ).grid(row=1,column=0,sticky=W)
        self.person1_ent = Entry(self)
        self.person1_ent.grid(row=1,column=1,sticky=W)

        Label(self,text="Person 2: "
              ).grid(row=1,column=2,sticky=W)
        self.person2_ent = Entry(self)
        self.person2_ent.grid(row=1,column=3,sticky=W)

        # create a label and text entry for a noun
        Label(self,text="Noun: "
              ).grid(row=2,column=0,sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2,column=1,sticky=W)        

        # create a label and text entry for a plural noun
        Label(self,text="Plural noun: "
              ).grid(row=2,column=2,sticky=W)
        self.plnoun_ent = Entry(self)
        self.plnoun_ent.grid(row=2,column=3,sticky=W)        

        # create a label for verb radio buttons
        Label(self,text="Verb: "
              ).grid(row=5,column=0,sticky=W)

        # create a variable for single body part

        self.verbs = StringVar()
        self.verbs.set(None)

        # create verb radio buttons
        verbs = ["finagle","juggle","snickersnee"]
        column = 1
        for part in verbs:
            Radiobutton(self,text=part,variable=self.verbs,value=part
                    ).grid(row = 5, column = column, sticky = W)
            column += 1

         # create a label for adjective check buttons
        Label(self,text="Adjective(s): "
              ).grid(row=4,column=0,sticky=W)

        # create itchy check button
        self.is_pompous = BooleanVar()
        Checkbutton(self,text="pompous",variable=self.is_pompous
                    ).grid(row=4,column=1,sticky=W)

        # create joyous check button
        self.is_super = BooleanVar()
        Checkbutton(self,text="supercalifragialistic",variable=self.is_super
                    ).grid(row=4,column=2,sticky=W)

        # create electric check button
        self.is_bumfuzzled = BooleanVar()
        Checkbutton(self,text="bumfuzzled",variable=self.is_bumfuzzled
                    ).grid(row=4,column=3,sticky=W)

        # create a submit button
        Button(self,text="Click for story",command=self.tell_story
               ).grid(row=6,column=0,sticky=W)
        
        # create text widget to display story
        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person1 = self.person1_ent.get()
        person2 = self.person2_ent.get()
        noun = self.noun_ent.get()
        plnoun = self.plnoun_ent.get()
        adjectives = []
        counter = 0
        if self.is_pompous.get():
            adjectives.append("pompous")
        if self.is_super.get():
            adjectives.append("supercalifragialistic")
        if self.is_bumfuzzled.get():
            adjectives.append("bumfuzzled")
        verb = self.verbs.get()

        # create the story
        if len(adjectives) != 2:
            story = "Hey, I said pick two adjectives!"
        else:
            story = "The pirates "
            story += person1 + " and " + person2
            story += " were terrors of the sea. "
            story += "They would "
            story += verb
            story += " their enemies just to see the look on their faces. In their final battle, "
            story += person1 + " took the most "
            story += adjectives[0]
            story += " boat they could find, and sailed it directly into the British "
            story += noun
            story += ". However, "
            story += person2 + " had other plans. "
            story += " While " + person1
            story += " was distracting the enemy, "
            story += person2 + " snuck into the British treasure room, grabbed all the "
            story += adjectives[1] + " " + plnoun
            story += ", and sailed away cackling. "
            story += "Poor " + person1
            story += "...or " + person2 + "?"

        #display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

# main
root = Tk()
root.title("Mad Lib")
#root.geometry("300x150")

# create a frame in the window to hold other widgets
app = Application(root)

#kick off the window's event loop
root.mainloop()
