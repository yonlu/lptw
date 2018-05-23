# Import argv from sys
from sys import argv
# assigns argv's arguments to script and input_file variables
script, input_file = argv
# defines the function print_all with one parameter called 'f'
def print_all(f):
    #it passes f to print and use a function called 'read'
    print(f.read())

def rewind(f):
    # Goes to the 1st byte of the file.
    f.seek(0)

def print_a_line(line_count, f):
    # prints the variable line_count and a line from the variable f
    print(line_count, f.readline())

# opens input_file and stores its value to current_file variable
current_file = open(input_file)

print("First let's print the whole file:\n")
# prints the entire file
print_all(current_file)

print("Now let's rewrind, kind of like a tape.")
# calls the rewind function, going to the first byte of the file.
rewind(current_file)

print("Let's print three lines:")
# assigns current_line to 1
current_line = 1
# calls print_a_line function, passing current_line (1) and current_file (opened input_file) as arguments.
print_a_line(current_line, current_file)

# assigns current_line to the current value of current_line + 1 => (1+1)
current_line += 1 # 2
print_a_line(current_line, current_file)

current_line += 1 # 3
print_a_line(current_line, current_file)
