fruit_to_color = {
    'banana':'yellow',
    'cherry':'red',
    'orange':'orange',
    'pear':'green',
    'peach':'orange',
    'plum':'purple',
    'pomegranate':'red',
    'strawberry':'red'}

#Invert fruit_to_color.
color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]
#If color not already a key in the accumulator,
#we will add color:[fruit] as an entry.

    if not (color in color_to_fruit):
        color_to_fruit[color] = [fruit]

#Otherwise, append fruit to the existing list.
    else:
        color_to_fruit[color].append(fruit)
