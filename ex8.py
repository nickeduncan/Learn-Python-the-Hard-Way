# variable set as a formattable string"
formatter = "{} {} {} {}"

# print variable formatted with numbers
print(formatter.format(1, 2, 3, 4))
# print variable formatted with words
print(formatter.format("one", "two", "three", "four"))
# print variable formatted with booleans
print(formatter.format(True, False, False, True))
# print variable formatted with itself
print(formatter.format(formatter, formatter, formatter, formatter))
# print variable formatted with strings
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))
