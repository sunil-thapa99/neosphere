# All parameters(arguments) in the python language are passed by reference. It means if you change what a parameter refers to within a 
# function, the change also reflects back in the calling function
# This works on mutable objects. Tuples is immutable, hence no change occurs
my_list = list(range(1, 5))
def info(arg):
	"""
		Function changes a passed list
	"""
	if isinstance(arg, list):
		# arg.append(6)
		arg.append(6)

	return arg

print(info(my_list))
print(my_list)