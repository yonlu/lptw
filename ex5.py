name = 'Lucas Sallada'
age = 21 # not a lie
height = 170 #cm
weight = 60 #kg
eyes = 'Hazel'
teeth = 'White'
hair = 'Dark Brown'

height_inches = height * 0.39
weight_pounds = weight * 2.2


print(f"Let's talk about {name}.")
print(f"He's {height}cm / {height_inches} inches tall.")
print(f"He's {weight}kg / {weight_pounds}lbs heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

