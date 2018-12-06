'''
	Any generator also is an iterator(not vice versa). Any generator, therefore is a factory that lazily produces values. Here is 
	the same Fibonacci sequence factory, but written as a generator
'''
# Generator Function
from itertools import islice
def fib():
	prev, curr = 0, 1
	while True:
		yield curr
		# Yield first return the value and pause the function until, for next value it is called
		prev, curr = curr, prev+curr

f = fib()
# f is now a generator object. Here no code gets executed but is in an idle state. 
# list(islice(f, 0, 100000) is iterator object
# list() starts to create a list and the start calling next() on islice() instance. The islice() will call next() of f instance.

# print(list(islice(f, 0, 100000)))

# for _ in range(100000):
# 	print(next(f))

numbers= [1, 2, 3, 4, 5]
a = (x*x for x in numbers)
# print(list(a)) This makes iterable object. And iterable object must be converted to iterator using iter(). 
print(next(a))
print(list(a))