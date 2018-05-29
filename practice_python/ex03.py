array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for number in array:
    if number < 5:
        print(f"{number}")

newArray = []

for number in array:
    if number < 5:
        newArray.append(number)

print(f"{newArray}")
