# Thinkful Lesson 6 Assignment 4
from __future__ import division
import random


# Classes
class Wheel(object):
	"""Bicycle wheels"""
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost

class Frame(object):
	"""Bicycle frames"""
	def __init__(self, material, weight, cost):
		self.material = material
		self.weight = weight
		self.cost = cost

class Bicycle(object):
	"""Complete Bicycle"""
	def __init__(self, name, manufactuer, wheel, frame):
		self.name = name
		self.manufactuer = manufactuer
		self.wheel = wheel
		self.frame = frame
		self.weight = self.wheel.weight * 2 + self.frame.weight
		self.cost = self.wheel.cost * 2 + self.frame.cost
	def retail(self, shop):
		return self.cost * ((self.manufactuer.percentage / 100) + 1) * ((shop.percentage / 100) + 1)
	def wholesale(self):
		return self.cost * ((self.manufactuer.percentage / 100) + 1)

class Manufactuer(object):
	"""Bicycle Manufactuers"""
	def __init__(self, name, percentage):
		self.name = name
		self.percentage = percentage
		self.bicycle_model = []
	def new_bike(self, model_name, wheel, frame):
		self.bicycle_model.append(Bicycle(model_name, self, wheel, frame))
	

class Shop(object):
	"""Bicycle shops"""
	def __init__(self, name, percentage):
		self.name = name
		self.percentage = percentage
		self.inventory = []
		self.profit = 0
	def add_bike(self, bicycle):
		num = random.randint(1,6)
		self.inventory.append({
			'bicycle': bicycle,
			'count': num
		})
		
			
	def sell_bike(self, bike_num):
		pass


class Customer(object):
	"""Customers"""
	def __init__(self, name, money):
		self.name = name
		self.money = money
		self.bike_list = []
	def buy(self, bicycle, shop):
		bike_name = bicycle['bicycle'].name
		self.money -= bicycle['bicycle'].retail(shop)
		self.bike_list.append(bicycle['bicycle'])
		shop.profit += bicycle['bicycle'].retail(shop) - bicycle['bicycle'].wholesale()
		for bike in shop.inventory:
			if bike['bicycle'].name == bike_name:
				bike['count'] = bike['count'] - 1











