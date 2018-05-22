from sys import argv

prompt = '> '

print("Hi! What is the file you would like to open?")
file = input(prompt)
file_txt = open(file)
print(file_txt.read())
