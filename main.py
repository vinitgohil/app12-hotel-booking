import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
credit_card_df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
card_security_df = pd.read_csv("card_security.csv", dtype=str)


class Hotel:

	def __init__(self, hotel_id):
		self.hotel_id = hotel_id
		self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

	def book(self):
		"""
		Book a hotel by changing its availability to No
		"""
		df.loc[df["id"] == self.hotel_id, "available"] = "no"
		df.to_csv("hotels.csv", index=False)

	def available(self):
		"""
		Checks if the Hotel is available
		"""
		availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
		if availability == "yes":
			return True
		else:
			return False


class ReservationTicket:

	def __init__(self, customer_name, hotel_obj):
		self.customer_name = customer_name
		self.hotel = hotel_obj

	def generate(self):
		content = f"""
		Thank you for your reservation!
		Here are your booking details:
		Name: {self.customer_name}
		Hotel Name: {self.hotel.name}
		"""
		return content


class CreditCard:
	def __init__(self, number):
		self.number = number

	def validate(self, expiration_date, holder, cvc):
		card_data = dict(number=self.number, expiration=expiration_date,
						 holder=holder.upper(), cvc=cvc)
		if card_data in credit_card_df:
			return True
		else:
			return False


class SecureCreditCard(CreditCard):

	def authenticate(self, given_password):
		password = card_security_df.loc[card_security_df["number"] == self.number, "password"].squeeze()
		if password == given_password:
			return True
		else:
			return False
6
print(df)
hotelID = input("Enter the id of the Hotel that you wish to book: ")
hotel = Hotel(hotelID)
if hotel.available():
	credit_card_no = input("Please enter you sixteen digit credit card no: ")
	credit_card_holder = input("Please enter the name of the credit card holder: ")
	expiry_date = input("Please enter expiry date of card: ")
	cvc = input("Please enter the CVC number of your card: ")
	credit_card = SecureCreditCard(number=credit_card_no)
	if credit_card.validate(expiration_date=expiry_date, holder=credit_card_holder, cvc=cvc):
		password = input("Please enter you credit card security password: ")
		if credit_card.authenticate(given_password=password):
			hotel.book()
			name = input("Enter your name: ")
			reservation_ticket = ReservationTicket(customer_name=name, hotel_obj=hotel)
			print(reservation_ticket.generate())
		else:
			print("Credit card authentication failed.")
	else:
		print("There was a problem with your payment. Please verify your card payment details.")
else:
	print(f"Hotel reservation for {hotel.name} is fully booked. Please try another hotel.")
