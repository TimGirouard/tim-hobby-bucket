# Write It
# Demonstrates writing to a text file

#Open write_it.txt

print("Creating a text file with the write() method.")
text_file = open("write_it.txt", "w")

#Fill the file

text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()

#Read the results

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

#Different Method

#Open write_it.txt

print("\nCreating a text file with the writelines() method.")
text_file = open("write_it.txt", "w")

#Fill the file

lines = ["Line 1\n",
         "This is line 2\n",
         "That makes this line 4\n"]
text_file.writelines(lines)
text_file.close()

#Read the results

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()



input("\n\nPress the enter key to exit.")
