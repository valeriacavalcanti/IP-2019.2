num = int(input("Número: "))
qtde = 0

for i in range(1, (num//2) + 1):
	if (num % i == 0):
		qtde += 1

qtde += 1

print(qtde)