#set cars number
cars = 100
#set free space in a car
space_in_a_car = 4
#set drivers number
drivers = 30
#old drivers number
old_drivers = drivers / 3
#passengers number
passengers = 90
#calculate numbers of cars that cannot be driven
cars_not_driven = cars - drivers
#calculate numbers of cars that can be driven
cars_driven = drivers
#calculate numbers of cars that driven by old drivers
cars_well_drived = old_drivers
#calculate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#calculate average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers and", old_drivers, "old drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
