from functools import partial

def multiply(x, y):
	return x * y

dbl = partial(multiply, 2)
print(dbl(4))
print(dbl(9))


def quadratic(a, b, c, x):
	return a*(x**2) + b * x + c

qua = partial(quadratic, 2, 3, 4)
print(qua(4))