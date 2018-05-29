name = input("What is your name? ")
favoriteNumber = input("By the way, what is your favorite number? ")
age = input("And how old are you? ")

age = int(age)
yearsToHundred = 100 - age

favoriteNumber = int(favoriteNumber)
i = 1
while i <= favoriteNumber:
    print(f"Hello {name}, you're going to be 100 years old in {yearsToHundred} years!")
    i += 1
