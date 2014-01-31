# Intersystems File I/O

import sys

#Open File Function

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

#Next Line Function

def next_line(the_file):
    """Return next line from the file."""
    line = the_file.readline()
    return line

def main():

    mod = int(input("What is the mod number?\n"))

    is_file = open_file("intersystems.txt", "r")

#Initialize all lines

    all_lines = ""
    first_line = ""
    last_line = ""
    skip_line = ""
    include_line = ""

#Add the first line

    first_line = next_line(is_file)
    all_lines = all_lines + first_line

#Add the last line
    
    while next_line(is_file):
        last_line = next_line(is_file)

    all_lines = all_lines + last_line

#Add the non-skip lines divisible by mod

    is_file = open_file("intersystems.txt", "r")

    tempy = next_line(is_file)
    if (len(tempy) % mod == 0) and ("skip" not in tempy.lower()) and (tempy not in all_lines):
        skip_line = skip_line + tempy
    
    while tempy:
        tempy = next_line(is_file)
        if (len(tempy) % mod == 0 and ("skip" not in tempy.lower())) and (tempy not in all_lines):
            skip_line = skip_line + tempy
    all_lines = all_lines + "\n" + skip_line

#Add the include lines not divisible by mod

    is_file = open_file("intersystems.txt", "r")

    tempy = next_line(is_file)
    
    if (not (len(tempy) % mod == 0)) and ("include" in tempy.lower()) and (tempy not in all_lines):
        include_line = include_line + tempy
        
    while tempy:
        tempy = next_line(is_file)
        if (not (len(tempy) % mod == 0)) and ("include" in tempy.lower()) and (tempy not in all_lines):
            include_line = include_line + tempy

    all_lines = all_lines + include_line

    print(all_lines)

main()
    
input("\nPress Enter to Exit.")
