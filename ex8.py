# Defines formatter to be 4 "string placeholders"
formatter = "{} {} {} {}"

# prints the formatter variable, while applying the format function to it, passing the values 1, 2, 3, and 4.
print(formatter.format(1, 2, 3, 4))
# Now it is passing the strings "one, two, three and four"
print(formatter.format("one", "two", "three", "four"))
# Now it is passing the values True, False, False and True (boolean values)
print(formatter.format(True, False, False, True))
# Now it is passing the formatter variable (which is just 4 string placeholders) to itself, so now each string placeholder will be populated by 4 "{}" (curly brackets)
print(formatter.format(formatter, formatter, formatter, formatter))
# Now it passes a line of text for each string placeholder, in the end making a poem.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
