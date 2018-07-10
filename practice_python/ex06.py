string = input("Please digit a word: ")
stringReverse = ''

for letter in string:
    stringReverse = letter + stringReverse

print(f"Here is the reversed word: {stringReverse}")

if string == stringReverse:
    print("It's a palindrome!")
else:
    print("Sorry, it's not a palindrome.")
