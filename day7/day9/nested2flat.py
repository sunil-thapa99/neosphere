a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([y for x in a for y in x])

# Equivalent to 
# b =[]
# for x in a:
# 	for y in x:
# 		b.append(y)
# print(b)

# b = []
# print([b.append(y) for x in a for y in x])
# b.append(y) => return None
# Output: [None, None, None, None, None, None, None, None, None]

# print(b)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([[y**2 for y in x]for x in a])

# Equivalent to 
c = []
for x in a:
	b =[]
	for y in range(len(x)):
		b.append(x[y] ** 2)
	c.append(b)
print(c)
