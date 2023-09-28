import pandas
# Import Abstract Base Class (ABC)
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
	# class Variable
	watermark = "The Hotel Booking Company"

	def __init__(self, hotel_id):
		# instance variables
		self.hotel_id = hotel_id
		self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

	def book(self):
		"""Book a hotel by changing its availability to no"""
		df.loc[df["id"] == self.hotel_id, "available"] = "no"
		df.to_csv("hotels.csv", index=False)

	def available(self):
		"""Check if the hotel is available"""
		availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
		if availability == "yes":
			return True
		else:
			return False

	# Class Method defines generic method defined for the class that is applicable for any instance
	@classmethod
	def get_hotel_count(cls, data):
		return len(data)

# Declare the Abstract Class of Ticket. Define ABC (Abstract Base Class). It is basically
# a blue print of any subclass that will use the abstract class as the base.
# any abstract method declared within the abstract class must be inherited when declaring the subclasses
# This enforces the programmer to use the abstract method(s) on any other classes that use this abstract class
class Ticket(ABC):

	@abstractmethod
	def generate(self):
		pass


class ReservationTicket(Ticket):
	def __init__(self, customer_name, hotel_object):
		self.customer_name = customer_name
		self.hotel = hotel_object

	def generate(self):
		content = f"""
		Thank you for your reservation!
		Here are you booking data:
		Name: {self.the_customer_name}
		Hotel name: {self.hotel.name}
		"""
		return content

	@property
	def the_customer_name(self):
		name = self.customer_name.strip()
		name = name.title()
		return name

	# Static Method is method applied when you want to perform
	# some generic utilities like calculations, transformations etc.
	# There is a blurred definition between static and class methods.
	@staticmethod
	def convert(amount):
		return amount * 1.2


class DigitalTicket(Ticket):
	def generate(self):
		return "This is your Digital Ticket"

	def download(self):
		pass
# hotel1 = Hotel(hotel_id="134")
# hotel2 = Hotel(hotel_id="188")
#
# print(hotel1.name)
# print(hotel2.name)
#
# print(hotel1.watermark)
# print(hotel2.watermark)
#
# print(Hotel.get_hotel_count(data=df))
#
# ticket = ReservationTicket(customer_name=" john smith ", hotel_object=hotel1)
# print(ticket.the_customer_name)
# print(ticket.generate())
#
# converted = ReservationTicket.convert(10)
# print(converted)
