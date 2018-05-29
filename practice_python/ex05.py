a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
finalList = []

c = []
for element in a:
    if element not in c:
        c.append(element)

print(f"Removing duplicates from first list: {c}")

d = []
for element in b:
    if element not in d:
        d.append(element)

print(f"Removing duplicates from second list: {d}")

for element in c:
    if element in d:
        finalList.append(element)

print(f"This is the Final List: {finalList}")
