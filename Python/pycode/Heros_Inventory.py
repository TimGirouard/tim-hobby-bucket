# Hero's Inventory
# Demonstrates tuple creation

# create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")

# create a tuple with some items
inventory = ("poop",
             "more poop",
             "even more poop",
             "and also poop")

# print the tuple
print("\nThe items in your bag are:")
print(inventory)

# Find out what item user wants

item_number = int(input("\nWhich item would you like? (1-4): "))
selected_item = inventory[item_number-1]
print ("\nYou selected the", selected_item)

# print each element in the tuple
print("\nThe items still in your bag are:")
for item in inventory:
    if item != selected_item:
        print(item)

input("\n\nPress the enter key to exit.")
