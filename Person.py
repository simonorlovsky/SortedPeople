from datetime import date

class Person:
	def __init__(self, firstName, lastName, birthDay, birthMonth, birthYear):
		self.fName = firstName
		self.lName = lastName
		self.age = date.today().year - birthYear
