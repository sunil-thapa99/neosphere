seq = list(range(1, 6))

total = 1 
for x in seq:
	total *= x

print(total)

# Recursive function 

def fact(n):
	if n == 1:
		return 1
	else:
		return(n*fact(n-1))
print(fact(5))