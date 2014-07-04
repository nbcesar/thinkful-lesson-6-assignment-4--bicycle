# Bicycle Model

# global lists in classes refer to same list when creating a new instance
# Models in a separate file
from bicycle_classes import Wheel, Frame, Bicycle, Manufactuer, Shop, Customer
import random

# Three frames
aluminum_frame = Frame('aluminum', 10, 500)
carbon_frame = Frame('carbon', 15, 250)
steel_frame = Frame('steel', 20, 100)

# Three wheels
mountain_wheel = Wheel('mountain', 10, 25)
road_wheel = Wheel('road', 5, 50)
hybrid_wheel = Wheel('hybrid', 8, 35)

# Two bicycle manufacturers
huffy = Manufactuer('huffy', 20)
huffy.new_bike('H1', road_wheel, aluminum_frame)
huffy.new_bike('H2', hybrid_wheel, aluminum_frame)
huffy.new_bike('H3', road_wheel, carbon_frame)
 
giant = Manufactuer('giant', 40)
giant.new_bike('G1', mountain_wheel, steel_frame)
giant.new_bike('G2', mountain_wheel, carbon_frame)
giant.new_bike('G3', road_wheel, steel_frame)

# One bicycle shop with  all 6 models carried
# Adds a random number of each bike
walmart = Shop('walmart', 20)
walmart.add_bike(huffy.bicycle_model[0])
walmart.add_bike(huffy.bicycle_model[1])
walmart.add_bike(huffy.bicycle_model[2])
walmart.add_bike(giant.bicycle_model[0])
walmart.add_bike(giant.bicycle_model[1])
walmart.add_bike(giant.bicycle_model[2])
	

# Three customers
customers = {
	'Cesar': Customer('Cesar', 300), 
	'Cristina': Customer('Cristina', 500), 
	'Unknown': Customer('Unknown', 1000)
	}


# Print name of weight of each bike at bike shop
print "Bicycles Walmart Carries"
for bike in walmart.inventory:
	print "{} weighs {} and costs {}".format(bike['bicycle'].name, bike['bicycle'].weight, bike['bicycle'].retail(walmart))

print
# Print name of customer and affordable bikes
print "Meet the customers"
for customer in customers:
	money = customers[customer].money
	print "{} has a budget of {} and can afford the following bikes:".format(customer, money)
	for bike in walmart.inventory:
		cost = bike['bicycle'].retail(walmart)
		if cost <= money:
			print "{}: ${}".format(bike['bicycle'].name, bike['bicycle'].cost)

print
#Prints initial inventory of bike shop
print "Walmart's inventory"
for bike in walmart.inventory:
	print "{}: {} remaining".format(bike['bicycle'].name, bike['count'])

print
# Each customer buys a bike
print "Customer purchases"
for customer in customers:
	for x in range(1,7):
		money = customers[customer].money
		bike = random.choice(walmart.inventory)
		bike_cost = bike['bicycle'].retail(walmart)
		if bike_cost < money:
			customers[customer].buy(bike, walmart)
			print "{} bought {} for {} and has {} remaining".format(customer, bike['bicycle'].name, bike_cost, customers[customer].money)
			break

print
# Remaining inventory and profits
print "Walmart's Remaining Inventory"
for bike in walmart.inventory:
	print "{}: {} remaining".format(bike['bicycle'].name, bike['count'])
print "Walmart has made a profit of {}.".format(walmart.profit)
# Action
#print steel_frame.cost
#print huffy.bicycle_model[0].name
#print len(walmart.inventory)
