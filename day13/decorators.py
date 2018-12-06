# def greet():
# 	print('Hello World')
# 	return 'Python is awesome'
# a = greet()
# b = greet 
# # b points on the same address as point by greet function

# print(a)
# print(b)
# print(b()) 

# def greet(name):
# 	def message():
# 		return 'Good Evening: '
# 	result = message() + name
# 	return result
# a = greet('Sunil')
# print(a)


# Function can be passed as a parameter to another function
# def greet(name):
# 	return 'Hello, ' + name
# def new(f, name):
# 	return f(name)

# print(new(greet, 'Sunil'))


# def h1(arg):
# 	return '<h1>' + arg + '</h1>'
# def h2(arg):
# 	return '<h2>' + arg + '</h2>'
# def h3(arg):
# 	return '<h3>' + arg + '</h3>'

# def func(fun, arg):
# 	return fun(arg)

# print(func(h1, 'Hello World'))
# print(func(h2, 'Sunil Thapa'))
# print(func(h3, 'Lol'))


# Decorator Example 1
# def decorate(func):
# 	def wrapper():
# 		return '<h1>'+ func() + '</h1>'
# 	# return wrapper()
# 	return wrapper

# def greet():
# 	return 'Sunil Thapa'

# # print(decorate(greet))
# greet = decorate(greet) # Returns function of type wrapper
# print(greet())


def decorate(func):
	def wrapper():
		return '<h1>'+ func() + '</h1>'
	# return wrapper()
	return wrapper
@decorate # Equivalent to decorate(greet)
def greet():
	return 'Sunil Thapa'
print(greet())

# Passing arguments to decorates
def tags(tag_name):
	def tags_decorator(func):
		def func_wrapper(name):
			return "<{0}>{1}</{0}>".format(tag_name, func(name))
		return func_wrapper
	return tags_decorator
a = 'p'
@tags(a)
def get_text(name):
	return "Hello: " + name
print(get_text('Sunil Thapa'))