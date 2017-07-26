# defines a function with two arguments and prints formatted strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

# calls functions with number arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# sets variables
amount_of_cheese = 10
amount_of_crackers = 50

# calls functions with variable arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calls function with addition in arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# adds to variable arugments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def cats(cats_count):
	print(f"You have {cats_count} cats.")
	print("That's too many cats!\n")

cats(2)

cats("two")

cats_count = 4
cats(cats_count)

cats(cats_count + 1)

cats(2 + 3)

cats("twenty" + "-five")

prompt = "How many cats you got? "
cats_count = input(prompt)
cats(cats_count)

cats_count = input(prompt)
cats(int(cats_count))

cats_count = input(prompt)
cats(int(cats_count) + 2)

cats_count = input(prompt)
cats(cats_count + " and a half")
