# Car is also an object of meta-class (type is a meta-class)
# __new__ is constructor, __init__ is intializer
class Car:
	def __init__(self, name, model=2018):
		'''
			Class with no parameter
				C = Car()
				C.name = 'Honda'
			with parameter
				c = Car('Honda')
				self.name = 'Honda'				
		'''
		self.name = name
		self.model = model
		self.set_type() # Alternative to c.self_type()
	def set_type(self):
		# This is instance method
		self.type = 'Electric'
	# def set_type():
		# pass
		# TypeError: set_type() takes 0 positional arguments but 1 was given
		# On self.set_type(), self is passing itself to the function

# On creating object, self then takes the object created
c = Car('Honda')
print(c.name)
print(c.model)
print(c.__dict__)
		