# Qs: Square all the objects inside a list
# <---------- Ans: Method => 1------------>
# a = [1, 2, 3, 4, 5]
# for x in range(len(a)):
# 	a[x] = a[x] ** 2
# print(a)

# <---------- Ans: Method => 2------------>
# a = [1, 2, 3, 4, 5]
# empty = []
# for x in a:
# 	empty.append(x**2)
# print(empty)


# <---------- Ans: Method => 3------------>
a = [1, 2, 3, 4, 5]
print([i**2 for i in a]) # List Comprehension
# print([for i in a: i**2]) => Invalid Syntax


# a = ['1', '2', '3', '4', '5', 'santosh']
# for x in range(len(a)):
	# isdecimal() or isnumeric()
# 	if a[x].isdecimal():
# 		a[x] = str(int(a[x]) ** 2)
# print(a)


a = ['1', '2', '3', '4', '5']
print([str(int(i)**2) for i in a]) # List Comprehension
# <generator object>
print(str(int(i)**2) for i in a) # if [] not given, it gives 


a = ['1', '2', '3', '4', '5', 'santosh']
print([str(int(i)**2) for i in a if i.isdecimal()])
# Equivalent to 
# for i in a:
#	if i.isdecimal():
# 		print(str(int(i) ** 2))
print([str(int(i)**2) if i.isdecimal() else i for i in a])
# Equivalent to 
# for i in a:
#	if i.isdecimal():
# 		print(str(int(i) ** 2))
#	else:
#		print(i)



# a = [5, 6, 4, 3, 7]
# for i in a[-3:]:
	# a[:3] => loop till 0, 1, 2 index
	# print(i)