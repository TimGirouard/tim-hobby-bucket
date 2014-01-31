# Trivia Challenge
# Trivia game that reads a plain text file

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
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

#Next Block Function

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []

    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)

    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    pointline = next_line(the_file)

    points = 0

    if pointline:

        points = int(pointline)

    return category, question, answers, correct, explanation, points

#Welcome Function

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to the Trivia Challenge!\n")
    print("\t\t", title, "\n")
    name = input("And what is your name, sir and/or madam?:")

    return name

def highscores(name, finalscore, file_name, text_file_name):
    """Creates highscore text doc."""

    import pickle, shelve

    #Bring in old names

    f = open(file_name, "rb")
    names = pickle.load(f)
    highscores = pickle.load(f)

    #Pickle the lists

    if len(names) <= 10:
        names.append(name)
        highscores.append(str(finalscore))
    i = 0
    if len(names) > 10:
        for i in range(len(names)):
            if finalscore > int(highscores[i]):
                names[i]=name
                highscores[i]=finalscore
                break
            i+=1

    f = open(file_name, "wb")

    pickle.dump(names, f)
    pickle.dump(highscores, f)
    f.close()

    #Unpickle the lists

    f = open(file_name, "rb")
    names = pickle.load(f)
    highscores = pickle.load(f)
    
    the_file = open_file(text_file_name, "w")
    i=0
    for i in range(len(names)):
        line = (names[i],"\t",str(highscores[i]),"\n")
        the_file.writelines(line)
        i+=1
    the_file.close()
    print("Names:",names)
    print("Highscores:",highscores)
    f.close()

#The old-fashioned way


    return names, highscores

#Main

def main():
    trivia_file = open_file("../Res/trivia2.txt", "r")
    title = next_line(trivia_file)
    name = welcome(title)
    score = 0

    #get first block

    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:

        #ask a question

        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])

        #get answer

        answer = input("What's your answer?:")

        #check answer

        if answer == correct:
            print("\nRight!", end="")
            score += points
        else:
            print("\nWrong.", end="")
        print(explanation)
        print("Score:", score, "\n\n")

        #get next block

        category, question, answers, correct, explanation, points = next_block(trivia_file)

    trivia_file.close()
    print("That was the last question!")
    print("Your final score is", score)
    highscores(name,score,"high_scores.dat","high_scores.txt")
main()
input("\n\nPress the enter key to exit.")
