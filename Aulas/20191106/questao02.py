numeros = []
soma = 0

for i in range(10):
	numeros.append(int(input()))
	soma += numeros[i]

media = soma // 10

for e in numeros:
	if (e % media == 0):
		print(e)