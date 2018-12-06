# To use abstract class
from abc import ABCMeta, abstractmethod
from math import pi
'''
	Meta class declares the behavior of class. 
	Class declares the behavior of object
'''
class Shape(metaclass=ABCMeta):
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def perimeter(self):
		pass

#  Can't instantiate abstract class Shape with abstract methods area, perimeter
# r = Shape()

class Rectangle(Shape):
	"""docstring for Rectangle"""
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length * self.breadth
	def perimeter(self):
		return 2 * (self.length + self.breadth)		

r = Rectangle(4, 5)
print(r.area(), r.perimeter())

# Inheritance
class Square(Rectangle):
	"""docstring for Square"""
	def __init__(self, side):
		super().__init__(side, side)

r = Square(5)
print(r.area(), r.perimeter())

class Circle(Shape):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius = radius
		
	def area(self):
		return pi * self.radius ** 2 
	def perimeter(self):
		return 2 * pi * self.radius
c = Circle(3)
print(c.area(), c.perimeter())

class Cylinder(Circle):
	"""docstring for Cylinder"""
	def __init__(self, radius, height):
		self.height = height
		super().__init__(radius)

	def area(self):
		circle_area = super().area()
		circle_perimeter = super().perimeter()
		return circle_perimeter * self.height + 2 * circle_area

	def perimeter(self):
		circle_perimeter = super().perimeter()
		return 2 * (circle_perimeter+self.height) 
c = Cylinder(5, 6)
print(c.area(), c.perimeter())
