# list size must be same
# If length is not same, then it discards other values whose matching are not present
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(list(zip(a)))
print(list((x+y) for x,y in zip(a, b)))
print(list(sum(x) for x in zip(a, b)))
print(list(map(sum, zip(a, b))))

from itertools import zip_longest
print(list(zip('xy', 'abcd')))
print(list(zip_longest('xy', 'abcd')))
print(list(zip_longest('xy', 'abcd' ,fillvalue='-')))

# itertools, functools, collection, re module(regex) => pyregex.com