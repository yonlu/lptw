number = input("Please type a number: ")
number = int(number)

if number % 4 == 0:
    print("It is divisible by 4!")
elif number % 2 == 0:
    print("It is even!")
else:
    print("It's odd!")
