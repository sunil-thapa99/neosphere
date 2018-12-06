#!/usr/bin/env python3

# for i in range(start, end, steps)

# for i in range(1, 11):print('*'*i)

# a = 2
# if a == 3:
# 	print('3')
# elif a == 5:
# 	print('5')

# for i in range(11, 0, -1):print('*'*i)

# for loop without break
# for i in range(10):
# 	print(i)
# else:
# 	print('Hello')


# <---------------------------------------------------------------------->
	# Else block is executed only when the for loop completes 
	# its iteration without breaking out of the loop
	# Similar with while loop
# <---------------------------------------------------------------------->

# <------------------------------->
# for loop with break

# for i in range(20):
# 	if i >= 15:
# 		break
# 	print(i)
# else:
# 	print('!!! For loop has completed !!!')

# <------------------------------->
# for loop with continue

# for i in range(20):
# 	if i >= 15:
# 		continue
# 	print(i)
# else:
# 	print('!!! For loop has completed !!!')

# <------------------------------->
# while loop with continue and break
a = 0
loop = 0
while a <= 10:
	if a == 5:
		break
	loop += 1
	a += 1
	# if a == 5:
	# 	continue
	print(a)
else:
	print('!!! While loop has completed its execution !!!')