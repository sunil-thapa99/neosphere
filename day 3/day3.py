
#Bitwise operator
5 ^ 2

# last operation result is stored in magic variable => _ 

# round(number, digit to occur)
round(1/3, 5)
# round(67/2)

# binary calculate
bin(5) # Ans: 0b101 <= b represents b
oct(8)
hex(10)

# a = ((5 ** 5) - 25) + 100  


# dir() => blank dir() gives variable used 

# del a => deletes a 

name = "sunil"

name[:] # Ans: 'sunil'

# name[startIndex:endIndex] endIndex => doesn't include

# name[:3] # Ans: 'sun' 

# name[:7] # Ans: 'sunil'

name.capitalize 
# <built-in method capitalize of str object at 0x7f8e535cd3e8>

# help(slice) => Slice
name[:-9] 

name[-9:]

name[-1:-4] # stop point must be greater than start point
name[-4:-1]

# name[startIndex:endIndex:step]  
name[::1] # Ans: 'sunil'


name[1:3:5] # start at index 1, go till index 3-1, increment by 5 in each step

name[::-5]

name[-3::-5]

# Check if attribute is present or not
's' in name

help(str.casefold)

# casefold
'SUnil'.casefold()

'SUnil'.casefold() == 'sunil' # Ans: True

# center(width[, fillchar])
# Centralise the word
'sunil'.center()
'sunil'.center(88)
'sunil'.center(41, '~')

'Hello World'.count('o')
'Hello World'.count('o', 5) # => Count till 5th step
'Hello World'.count('o', 0, 7) # => Count from 0 to till 7th step
 
# ljust => left justify
# rjust => right justify

'Hello World'.strip()	# strip() removes spaces

# l, rFucntion defines for left and right

'24442'.zfill(9)

'hello world'.title() # Capitalize first index of a word

'hElLo'.swapcase() # swap lower and upper

hash('sunil')

'sunil'.startswith('s') # Compares

'sunil'.endswith('s') # False
'sunil'.endswith('l') # True

'sunil \n thapa'.splitlines()

'sunil thapa'.split()

'sunilthapa'.split('t') # Split from t, t excluded

'sunilthapa'.rsplit('t') 

'sunilthapa'.partition('a') # Split from a, a included

'sunilsunil'.partition('s') # Split from a, a included


