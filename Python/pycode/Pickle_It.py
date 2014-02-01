# Pickle It
# Demonstrates pickling and shelving data

import pickle, shelve

#Pickle the lists

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

f = open("../Res/pickles1.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

#Unpickle the lists

print("\nUnpickling lists.")
f = open("../Res/pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print("Variety:",variety)
print("Shape:",shape)
print("Brand:",brand)
f.close()

#Create a shelf

print("\nShelving lists.")
s = shelve.open("../Res/pickles2.dat")

s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]

s.sync()

# make sure data is written

print("\nRetrieving lists from a shelved file:")
print("Brand:", s["brand"])
print("Shape:", s["shape"])
print("Variety:", s["variety"])

s.close()

input("\n\nPress the enter key to exit.")
