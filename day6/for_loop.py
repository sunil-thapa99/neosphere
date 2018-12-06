#!/usr/bin/env python3

for i in (1, 2, 3, 4):
	print(i)

for i in (1,):
	print(i)

for i in 1: print(i) # int is not iterable

a = (1)
b = (1,)

type(a) # => int
type(b) # => Tuple


name = 'Sunil'
for j in name: print(j)

for j in 's': print(j) # s in 0th index 

for j in '': print(j) # doesn't print j as there is no value to evaluate

for j in True: print(j) # bool isn't iterable object

for j in True, False: print(j) # similar to tuple (True, False)


# Capitalize the objects inside list
names = ['sunil', 'ram', 'shyam']
for name in names: 
	print(name.capitalize())
	print(name.upper())
	

names = ['sunil', 'ram', 'shyam', 15]
for name in names: 
	print(name.upper() if isinstance(name, str) else name)