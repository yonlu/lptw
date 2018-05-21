# Assigns 10 to types_of_people variable
types_of_people = 10
# Assigns "There are {types_of_people} types of people." to the variable x
x = f"There are {types_of_people} types of people."

# Assigns the stirng with value "binary" to the binary variable.
binary = "binary"
# Assigns "don't" string to do_not variable
do_not = "don't"
# Assigns "Those who know {binary} and those who {do_not}." string to the variable y
y = f"Those who know {binary} and those who {do_not}."

# It prints the variable 'x'
print(x)
# It prints the variable 'y'
print(y)
# It prints "I said (variable x value)"
print(f"I said: {x}")
# It prints "I also said '(variable y value)'"
print(f"I also said: '{y}'")
# Sets hilarious to the value of False
hilarious = False
# Sets joke_evaluation to "Isn't that joje so funny? {}"
joke_evaluation = "Isn't that joke so funny?! {}"
# Prints joke_evaluation and formats the value passed to this method
print(joke_evaluation.format(hilarious))

# Assigns w as "This is the left side of.."
w = "This is the left side of..."
# Assigns e as "a string with a right side."
e = "a string with a right side."

# Prints w and then concatinates e into the resulting string.
print(w + e)
