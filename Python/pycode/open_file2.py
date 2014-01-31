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

def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter. The lines should have the
    newline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))

    return matches

def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    file.write(sentences)

def main():

    data_file = open_file("../Res/trivia2.txt", 'r')
    print(lines_startswith(data_file, 'C'))
    data_file2 = open_file("../Res/File_write.txt", 'w')
    write_to_file(data_file2, ["This is a sentence.",
    "Here is sentence number two.", "And here is number three."])

main()
    
input("\nPress Enter to Exit.")
