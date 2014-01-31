def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)

    except IOError as e:
        print("Unable to open the file", file_name, "Ending program. \n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()

    else:
        return the_file

def main():

    data_file = open_file("trivia2.txt", 'r')
    for line in data_file:
        print(line.rstrip('\n'))

main()
    
input("\nPress Enter to Exit.")
