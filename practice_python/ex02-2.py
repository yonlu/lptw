num = input("Please enter a number to be checked: ")
num = int(num)

check = input("Please enter a check number: ")
check = int(check)

if num % check == 0:
    print(f"{num} can be divided evenly by {check}!")
else:
    print(f"Sorry! {num} can not be divided evenly by {check}...")
