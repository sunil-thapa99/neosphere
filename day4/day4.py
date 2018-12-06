#!/usr/bin/env python3

# Life is fun with python

# Bitwise operands: &, |, ^, ~, <<, >>

name = 'Sunil Thapa'
length = len(name)

# indexFirst = name.index('q') # Substring not found
# firstIndex = name.find('q')	# Ans: -1 => Not found 

# secondIndex = name.rfind('a')
# secondIndex = name.find('a', (firstIndex+1), length)

#Join method of string

a = ['s', 'u', 'n', 'i', 'l']
'*'.join(a) # joins * in every element

name.replace('a', 'b')
name.replace('a', 'b', 1) # replaces 1st a by b

# take input 
# name = input('Enter your name: ')
# print('Your name is: ', name.title())

name = input('Enter your name: ')
age = input('Enter your age: ')

if name.isalpha() and age.isnumeric():
	# print('Your name is: %s, age is: %s' %(name, age))
	# print('Your name is: {}, age is: {}'.format(name.title(), age))
	# print('Your name is: {1}, age is: {0}'.format(age, name.title()))
	# print('Your name is: {name}, age is: {age}'.format(age = age, name = name.title()))
	print(f'Your name is: {name}, age is: {age}') # From python 3.6+, f => formatting
else:
	print('lol')
