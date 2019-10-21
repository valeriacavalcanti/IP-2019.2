menor = maior = int(input("Número: "))

for i in range(1, 10):
	num = int(input("Número: "))
	if (num < menor):
		menor = num
	elif (num > maior):
		maior = num

print(f"Maior = {maior}")
print(f"Menor = {menor}")