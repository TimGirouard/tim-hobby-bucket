# Pickle It
# Demonstrates pickling and shelving data

import pickle, shelve

#Pickle the lists

#print("Pickling lists.")
#names = ["Johnny", "Jimmy"]
#highscores = ["5", "5"]

#f = open("../Res/high_scores.dat", "wb")

#pickle.dump(names, f)
#pickle.dump(highscores, f)
#f.close()

#Unpickle the lists

print("\nUnpickling lists.")
f = open("../Res/high_scores.dat", "rb")
names = pickle.load(f)
highscores = pickle.load(f)

print("Names:",names)
print("Score:",highscores)
f.close()

input("\n\nPress the enter key to exit.")
