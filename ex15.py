# includes the argv module
from sys import argv

# sets scripta and filename as variables from CLI
script, filename = argv

# opens the file and sets it to a var
txt = open(filename)

# prints text formatted with the filename
print(f"Here's your file {filename}:")
# prints the content of the file
print(txt.read())

# prompt
print("Type the filename again:")
# prompts for the filename
file_again = input("> ")

# opens the file inputted
txt_again = open(file_again)

# prints the content of the file
print(txt_again.read())
