#!/usr/bin/env python3

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = []
for x in a:
	temp.extend(x)
a = temp.copy()
print(a)