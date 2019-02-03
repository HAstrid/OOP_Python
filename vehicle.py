class Car:
	def model(self):
		print("Model: new")

class Bike:
	def company(self):
		print("HD")

class Truck:
	def type(self):
		print("truck")

class Vehicle:
	def call_car(self):
		Car()
	def call_bike(self):
		Bike()
	def call_truck(self):
		Truck()

v=Vehicle()
while(True):
	print("1.Car\n2.Bike\n3.Truck\n4.Exit\n")
	ch=int(input("Enter choice:"))
	if ch==1:
		v.call_car()
	elif ch==2:
		v.call_bike()
	elif ch==3:
		v.call_truck()
	else:
		break
