class A():
	def area(self):
		print('Im A')

class B(A):
	def area(self):
		super().area()
		print('Im B')

# class C(A):
# 	def area(self):
# 		super().area()
# 		print('Im C')

# class D(B, C):
# 	def area(self):
# 		super().area()
# 		print('Im D')

class C(B, A):
	def area(self):
		super().area()
		print('Im C')

a = A()
b = B()
c = C()
a.area()
print('-----------------')
b.area()
print('-----------------')
c.area()