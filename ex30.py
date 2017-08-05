people = 30
cars = 30
trucks = 35


# prints line if more cars than people
if cars > people:
    print("We should take the cars.")
# prints line if less cars than people
elif cars < people:
    print("We should not take the cars.")
#prints line if equal number of cars and people
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
