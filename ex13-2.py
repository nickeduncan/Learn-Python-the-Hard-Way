from sys import argv

script, first, second = argv

print("Thanks for using", script)
var = input(f"What is your {first}? ")
var2 = input(f"What is your {second}? ")
print(f"Glad to know you're {var} {var2}!")
