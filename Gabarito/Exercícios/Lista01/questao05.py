menor = maior = float(input("Número: "))

for i in range(1, 100):
	num = float(input("Número: "))
	if (num < menor):
		menor = num
	elif (num > maior):
		maior = num

print(f"Maior = {maior}")
print(f"Menor = {menor}")