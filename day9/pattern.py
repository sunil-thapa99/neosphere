a = [5, 6, 4, 3, 7]

for x in range(len(a)):
	for y in range(0, (x+1)):
		print(a[y], end=' ') # end='\n' in default
		# print(a[y], sep=' ')
	print('\n')