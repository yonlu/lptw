array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = input("Please digit a number: ")
number = int(number)

newArray = []

for element in array:
    if element < number:
        newArray.append(element)

print(f"{newArray}")

