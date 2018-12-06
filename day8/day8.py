#!/usr/bin/env python3

# Datastructure = Collection of data types

dir(__builtins__) # Built-in

# Data structure => "list => [], tuple => (), set => set(), dict => {}" 

a = []
dir(a)
dir(a)[-11:] # provides list from last

a.append(1)

# Default return is 'None'

r = a.append(3)
type(r) # => NoneType, since append returns None

# immutable(no change) and mutable(Change)# 
# Ex: string is immutable (name ='sunil', name.upper())
# Ex: list is mutable (a = [], a.append(3))

# a.count(value) => Counts the appearance of value in the list
a = [1, 2, 3, 4, 5, 2, 6, 2, 7]
a.count(2)

# a.index(value, start=0, stop=9223372036854775807) => provides index of number
# help(a.index)

# a.sort() => sorts in ascending order
# a.sort(key = None, reverse = False)

# a.insert(index, value)

# a.pop(index) => default pops from -1(last)

# a.remove(value)
 
# a.reverse()

# a.extend(iterable)

b = [1, 2, 3]
a.extend(b)

# c = a.copy()


# [list] * int
[1] * 2 # => [1, 1]
# m = [1, 2, 3] => m *= 3 => [1, 2, 3, 1, 2, 3, 1, 2, 3]

t = [3, 4, 5]
t.__mul__(2) # == t *= 2
t.__add__([1, 2]) # == t + [1, 2]

help(list.__mul__)
# __mul__ => self * value
# __mul__ => value * self
# __imul__ => self *= value
# __reversed__ => reverse the order

# value in list => calls __contains__
# value not in list

[].__sizeof__()
''.__sizeof__()
5.__sizeof__()

del a[2:10] # start, end

t = [4, 'lol', True, 1.2, None]
for i in t:
	print(type(i))
