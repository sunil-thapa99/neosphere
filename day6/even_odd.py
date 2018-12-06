#!/usr/bin/env python3

a = 0
print('<-------------- Going Inside Of Loop -------------->')
while a <= 20:
	# if a % 2 == 0:
	# 	print('{} Even'.format(a))
	# else:
	# 	print('{} Odd'.format(a))
	# a += 1

	# print('{} Even'.format(a)) if a % 2 == 0 else print('{} Odd'.format(a))
	print('{} Even'.format(a)) if a % 2 is 0 else print('{} Odd'.format(a))
	a += 1 

print('<-------------- Finally Out Of Loop -------------->')