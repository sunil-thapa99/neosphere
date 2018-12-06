#!/usr/bin/env python3

first = 0
second = 1

# first, second = 0, 1

while first <= 50:
	print(first)
	# temp = first + second
	# first = second
	# second = temp
	first, second = second, first + second
