user_amount = [('sunil', 150000), ('ram', 15200), ('shyam', 14020), ('hari', 16200), ('sita', 20000)]

# filter(function, iterable)
# map(function, iterable)
# Code below, passed user_amount which then break down into user that stores tuple of user_amount
total = sum(map(lambda user : user[1]*0.05, user_amount))
print(total)

# def interest_calculate(amount):
# 	return [((x*5)/100) for x in amount]

# def user():
# 	total_amount = 0
# 	amount = [x[1] for x in user_amount]

	# total = interest_calculate(amount)
	# Lambda expression for above statement. No need of function 
# 	x = lambda a : [((x*5)/100) for x in a]
# 	total = x(amount)
	
# 	print(total)
# 	print('Final Result')
# 	for x in total:
# 		total_amount += x
# 	print(total_amount)

# user()

# In python, ["", [], (), {}, 0, 0.0, None, False] treat as False 

cities = ['ktm', None, -1, 0, '', 'pkr', False, [], {}, ()]
# print(list(filter(None, cities)))
print(list(filter(lambda city: city or city is 0, cities)))
