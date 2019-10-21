a = int(input('A: '))
b = int(input('B: '))

if (a > b):
	a, b = b, a

if (a % 2 == 0):
	a += 1

for i in range(a, b + 1, 2):
	print(i)