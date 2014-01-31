# Click Counter
# Demonstrates binding an event with an event handler

from tkinter import *

class Application(Frame):
    """ A GUI application which counts button clicks. """

    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # the number of clicks
        self.create_widget()

    def create_widget(self):
        """ Create a button that displays number of clicks. """
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

# create a frame in the window to hold other widgets
app = Application(root)

#kick off the window's event loop
root.mainloop()
