def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(20, 1)
height = subtract(78, 4)
weight = multiply(60, 2)
iq = divide(400, 2)

print(f"Age: {age}. Height: {height}. Weight: {weight}. IQ: {iq}")

# A puzzle for the extra credit, type it anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

#divide => iq(400/2 => 200) / 2 => 100
# multiply => weight(60 * 2) * iq-result(100) => 120 * 100 => 12000
#subtract => height(78 - 4) - 1200 => 74 - 12000 => -11926
#add age(20 + 1) + (-11926) => 21 - 11926 => 11905
print("That becomes: ", what, "Can you do it by hand?")
