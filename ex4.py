# number of cars
cars = 100
# availabe seats per car
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of empty cars
cars_not_driven = cars - drivers
# number of cars to be driven
cars_driven = drivers
# total available seats
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers in each used car
average_passengers_per_car = passengers / cars_driven 


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There wil be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
