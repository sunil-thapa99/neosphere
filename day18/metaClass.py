"""
	Meta class inherite from type class
	Meta class is called factory of class
"""

class Shape(type):
	# Meta class => __init__, __new__, __call__ needs to be in metaclass
	def __new__(cls, name, bases, dictionary):
		# bases => base class name, cls => ClassName to be created
		x = super().__new__(cls, name, bases, dictionary)
		print(cls)
		print(name)
		print(bases)
		print(dictionary)
		x.attr = 100
		return x
		# x is the new class name to be made
		

class Circle(metaclass=Shape):
	# def __init__(self, arg):
	# 	super(Shape, self).__init__()
	# 	self.arg = arg
	pass
print(Circle.attr)
		