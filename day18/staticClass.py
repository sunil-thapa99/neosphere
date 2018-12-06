import math
class Circle(object):
	def __init__(self, radius):
		self._radius = radius
	
	def area(self):
		return math.pi*(self._radius**2)

	def perimeter(self):
		return 2*math.pi*self._radius

	@staticmethod
	# No relation with objects so self doesnot get passed as a parameter
	def _radius_to_diameter(radius):
		return radius*2

	# Classmethod is factory method
	@classmethod
	def unitCircle(cls):
		return cls(1)
		# Return 1 radius to class

	@property
	def diameter(self):
		# return self._radius * 2
		r = self._radius
		return self._radius_to_diameter(r)

if __name__ == '__main__':
	c = Circle(5)
	print(c.area())
	print(c.perimeter())
	print(c.diameter) # Making property

	u = c.unitCircle()
	print(u.area())
	print(u.perimeter())
	print(u.diameter)
	print(type(u))