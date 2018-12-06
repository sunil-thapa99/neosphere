#!/usr/bin/env python3

teslist = [10, 20, 30]

# enumerate(iterable, counterStart=0)

# for i, value in enumerate(teslist):
	# i = counter, value = value 
	# unpacking the (i, value)
# 	print(i, ':', value)

# Without unpacking 
for value in enumerate(teslist):
	# value = tuple containing (counter, value)
	print(value)


# for i, value in enumerate(teslist, 5):
# 	print(i, ':', value)

print('\n<---------------------------->\n')

days = ('sun', 'mon', 'tues', 'wed', 'thur', 'fri', 'sat')
for i, day in enumerate(days):
	print(i, ':', day)