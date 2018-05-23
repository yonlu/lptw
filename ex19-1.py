from sys import argv

script, firstArg, secondArg = argv

def my_function(*args):
    arg1, arg2 = args
    print(f"You said {arg1} and then {arg2}!")

# First way: input
print("The first way is through input!")
first = input("What do you wanna say? ")
second = input("And after that? ")
my_function(first, second)

# Second way: hard-coded variables
print("The second way is using variables")
first = "Foo"
second = "Bar"
my_function(first,second)

# Third way: hard-coded arguments
print("The third way is just passing arguments directly in the code")
my_function("Seems like", "I can redefine variables!")

# Fourth way: using argv
print("The fourth way is using argv")
my_function(firstArg, secondArg)

# Fifth way: using another function
print("And the fifth is using another function!")
def return_strings():
    return ("what is this")
# I hope this works?
my_function(return_strings(), return_strings())
