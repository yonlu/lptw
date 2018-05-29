number = input("Please type a number: ")
number = int(number)

myArray = []

i = 1
for i in range(i, number):
    if number % i == 0:
        myArray.append(i)

print(f"{myArray}")

