# import argv module from sys
from sys import argv

#assigns argv arguments to script and filename variables
script, filename = argv
#open the file with the value of filename and assign it to variable 'x'
txt = open(filename)

#prints the filename
print(f"Here's your file {filename}:")
#prints out the the file content to the terminal
print(txt.read())
txt.close()
