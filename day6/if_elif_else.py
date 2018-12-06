#!/usr/bin/env python3

# Conditional Statement

# age = input("What is your age: ")
# age = int(age)

# age = int(input("What is your age: "))

# if age < 0 or age > 120:
# 	print("Invalid entry!!!")
# elif age <= 2:
# 	print("!!! Infant !!!")
# elif age <= 12:
# 	print("!!! Child !!!")
# elif age <= 19:
# 	print("!!! Teenager !!!")
# elif age <= 40:
# 	print("!!! Adult !!!")
# else:
# 	print("Your age is {}. You have become old".format(age))

# View: "import this"

o_marks = 55
# is_pass = True if o_marks > 40 else False # Ternary operator
is_pass = "Pass" if o_marks > 40 else "Fail"
print(is_pass)

a = [3, 4, 5] 
# {3, 4, 5} => set
if 5 in a:
	print('True')
# 6 in a => False (No if needed)

# list = []
# set = set()
# dictionary = {}
# tuple = ()
