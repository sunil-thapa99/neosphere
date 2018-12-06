# A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 
# However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.

# message = 'new'
# def hello(message):
# 	# "This is the enclosing function"
# 	print('Hello: ', message)
# 	def greet():
# 		global message
# 		message = 'Good Evening'
# 	#	"The nested function"
# 		print('Greet: ', message)

# 	greet()

# hello("Good Morning")
# print('Outer', message)


'''
	Nonlocal keyword is used to change within the parent scope from child scope
'''
# message = 'new'
# def hello(message):
# 	# "This is the enclosing function"
# 	print('Hello: ', message)
# 	def greet():
# 		nonlocal message
# 		message = 'Good Evening'
# 	#	"The nested function"
# 		print('Greet: ', message)

# 	greet()

# hello("Good Morning")
# print('Outer', message)



def hello(message):
	def greet():
		print('Greet: ', message)

	return greet
a = hello("Good Morning")
# print(type(a))
a()

# Closures can avoid use of global variables and provides some form of data hiding. (Eg. When there are few methods in a class,
# use closures instead)