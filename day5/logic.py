#!/usr/bin/env python3
1 == True # true
1 is True # False => as === (diff datatype)

#  At 'and' if numbers are non-zero, priority is given to last one
# At 'or' if number is non-zero, priority is given to first one
# At 'or', 0 has no value
1 and 0 # 0
0 and 1 # 0
5 and 6 # 6
0 and 6 # 0
0 and 0 # 0

1 and -1 # 1
-1 and 1 # 1

True and 1 # 1
1 and True # True
0 and True # 0

1 and 5 or 0 # 5
1 and 0 or 1 # 0

1 or 0 and 0 # 1

# precedence order and, or

1 or 4 and 2 # 1
0 or 4 and 2 # 2

a = [3, 2, 5]
5 in a # True
1 in a # False
5 not in a # False

not 1 # False
not 0 # True
not True # False
not False # True

1 & 1 # 1 
5 & 3 # 1 
32 & 55 # 32
1 | 0 # 1
1 & 0 | 1 # 1
1 != 5 # True

32 >> 3
32 << 3

# calculate ASCII
ord('a')
ord('A')

# Calculate character of given ASCII
chr(67) # C

True + 9 # 10 => 1 + 9 = 10

5.001 > 5 # True
5.0000000000000001 > 5 # False

