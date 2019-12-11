a = [0] * 3
b = [0] * 3
c = [0] * 3

for i in range(3):
	a[i] = [0] * 3
	b[i] = [0] * 3
	c[i] = [0] * 3

for i in range(3):
	for j in range(3):
		a[i][j] = int(input())

for i in range(3):
	for j in range(3):
		b[i][j] = int(input())

for i in range(3):
	for j in range(3):
		for k in range(3):
			c[i][k] += a[i][j] * b[j][k]


for i in range(3):
	for j in range(3):
		print(c[i][j])