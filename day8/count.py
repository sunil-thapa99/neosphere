#!/usr/bin/env python3
datatype = input('Input Datatype:')
if datatype.upper() == 'INT':
	datatype = 1
elif datatype.upper() == 'FLOAT':
	datatype = 1.1
elif datatype.upper() == 'BOOL':
	datatype = True
elif datatype.upper() == 'NONE':
	datatype = None
elif datatype.upper() == 'LIST':
	datatype = []
elif datatype.upper() == 'TUPLE':
	datatype = ()

a = dir(datatype)
b = 0
list = []
while b < len(a):
	flag = True
	c = a[b]
	for x in c:
		# print(c[x])
		if(x == '_'):
			flag = False
			break
	if flag == True:
		list.append(c)
		# pass
	b += 1
print(list)
print(len(list))
