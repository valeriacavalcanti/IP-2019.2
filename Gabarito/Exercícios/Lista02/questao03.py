num = int(input("Número: "))
soma = 0

for i in range(1, (num//2) + 1):
	if (num % i == 0):
		soma += i

if (soma == num):
	print("Perfeito")
else:
	print("Não Perfeito")