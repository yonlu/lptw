# Assigns the value 100 to the variable cars
cars = 100
# Assigns the value of 4.0 (?) to variable space_in_a_car
space_in_a_car = 4
# Assigns the value of 30 to drivers variable
drivers = 30
# Assigns the value of 9- to passeners variable.
passengers = 90
# Assigns the value of cars - drivers to variable cars_not_driven.
# Since cars is 100 and drivers has the value of 30
# 100 - 30
# 70
cars_not_driven = cars - drivers
# Assigns the value of drivers to cars_driven (30)
cars_driven = drivers
# Assigns the value of the expression (cars_driven * space_in_a_car) to carpool_capacity variable
# cars_driven = 30, space_in_a_car = 4.0
# 30 * 4.0
# 120.0
carpool_capacity = cars_driven * space_in_a_car
# Assigns the value passengers / cars_driven to variable average_passengers_per_car
# passengers = 90, cars_driven = 30
# 90 / 30
# 3
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")


