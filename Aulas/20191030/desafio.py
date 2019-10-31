soma = 0
numeros = [0]*10

for i in range(10):
	numeros[i] = int(input(f'Número {i}: '))
	soma += numeros[i]

media = soma / 10

for i in range(10):
	if (numeros[i] > media):
		print(numeros[i])

print(f'media = {media}')
print(numeros)

for i in range(10):
	print(numeros[i])

for i in range(10):
	print(numeros[i], end=' ')