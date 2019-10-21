n, x, y = input("N X Y = ").split()
n, x, y = int(n), int(x), int(y)

for i in range(x, y + 1):
	if (i % n == 0):
		print(i)