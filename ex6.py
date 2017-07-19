# sets a variable to a number
types_of_people = 10
# sets an interpolated string to a variable
x = f"There are {types_of_people} types of people."

# sets a string to a variable
binary = "binary"
# sets a string to a variable
do_not = "don't"
# sets a formatted string to a variable
y = f"Those who know {binary} and those who {do_not}."

# prints a formatted string
print(x)
print(y)

# prints a formatted string withing a formatted string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# sets a variable to false
hilarious = False
# sets a formattable string to a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# prints a string formatted with a boolean variable
print(joke_evaluation.format(hilarious))

# sets a variable to a string
w = "This is the left side of..."
e = "a string with a right side."

# concatenates two strings
print(w + e)

