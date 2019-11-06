numeros = [0]*10

for i in range(10):
	numeros[i] = int(input())

# positivos
print("positivos:")
for i in range(10):
	if (numeros[i] > 0):
		print(numeros[i], end=' ')


print('\nPares:')

# pares
for i in range(10):
	if (numeros[i] % 2 == 0):
		print(numeros[i], end=' ')