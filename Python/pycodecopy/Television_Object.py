#Television Object

class Television(object):
    """The television"""
    def __init__(self, channel=1, volume=1):
        self.channel = channel
        self.volume = volume

    def display(self):
        print("The television is set to channel", self.channel,
        "and the volume is set to", self.volume, "now.\n")

    def change_channel(self, newchannel):
        self.channel = newchannel

    def change_volume(self, newvolume):
        self.volume = newvolume

def main():
    tv = Television()
    tv.display()
    choice = None
    while choice != "0":
        print \
        ("""
        Television Program

        0 - Quit
        1 - Display the settings
        2 - Change the channel
        3 - Change the volume
        """)

        choice = input("Choice:")
        print()

        # exit
        if choice == "0":
            print("Thank you for playing.  Good-bye.")

        #check the settings
        elif choice == "1":
            tv.display()

        elif choice == "2":
            channel = 0
            while channel < 1 or channel > 250:
                channelstring = input("What channel would you like to watch (1-250)")
                try:
                    if 1 <= int(channelstring) <=250:
                        channel = int(channelstring)
                    else:
                        print("That is not a valid volume setting.")  
                except ValueError:
                    print("That is not a valid channel.")  
            tv.change_channel(channel)

        elif choice == "3":
            volume = 0
            while volume < 1 or volume > 50:
                volumestring = input("What channel would you like to watch (1-50)")
                try:
                    if 1 <= int(volumestring) <=50:
                        volume = int(volumestring)
                    else:
                        print("That is not a valid volume setting.")  
                except ValueError:
                    print("That is not a valid volume setting.")  
            tv.change_volume(volume)

        #any other choice
        else:
            print("\nSorry, but", choice, "is not a valid selection.")

main()
("\n\nPress the enter key to exit.")
