matriz = [0] * 6
for i in range(6):
	matriz[i] = [0] * 6

print(matriz)

for i in range(6):
	for j in range(6):
		print(matriz[i][j], end=' ')
	print()

print()

for i in range(6):
	matriz[i][i] = 1

for i in range(6):
	for j in range(6):
		print(matriz[i][j], end=' ')
	print()


for i in range(6):
	for j in range(6):
		if (matriz[i][j] == 1):
			print('*', end=' ')
		else:
			print(' ', end=' ')
	print()






