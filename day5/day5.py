#!/usr/bin/env python3
# Life is fun with python

name = "I Love Python!"
name = name.split()
nameWithoutSpace = ''.join(name)
print(len(nameWithoutSpace))
# print(len(name))

print('<-------------------->')

# <---------------- Alternative ------------------>
name = "I Love Python!"
print(len(name))
print(name.count(' '))
print(len(name) - name.count(' '))

print('<-------------------->')

my_string = 'I l@v# pyth$on!'
my_string = ''.join(my_string.split())
print(my_string)
count = 0
for x in my_string:
	if x.isalpha() == False:
		count += 1 


print(count)

		