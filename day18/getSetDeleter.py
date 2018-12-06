class Employee:
	__Tax = 0.6

	def __init__(self, name, salary):
		self._name = name 
		self._salary = salary

	# Used to make function act as a property/attribute of a class 
	@property
	def salary(self):
		tax_amount = self._salary * (Employee.__Tax / 100)
		return self._salary - tax_amount
	
	@property
	def name(self):
		return self._name

	# Setter => @methodname.setter
	@salary.setter
	def salary(self, value):
		self._salary = value

	# Deleter => @methodname.deleter
	@salary.deleter
	def salary(self):
		del self._salary

if __name__ == '__main__':
	e = Employee('Ram', 120000)
	# print(e.salary) # Has no attribute unless an decorator is made
	print(e._salary)
	# print(e.salary())
	print(e.salary) # Now, salary acts as salary()
	# e._salary = 140000
	e.salary = 10000
	print(e.__dict__)
	print(e.name)

	del e.salary
	print(e.__dict__)
