#!/usr/bin/env python3

number = 2
while number < 100:
	# flag = True
	for a in range(2, (int(number/2)+1)):
		if number % a == 0:
			# flag = False
			break
	# if flag:
	else:
		print(number)
	number += 1


# For-else 