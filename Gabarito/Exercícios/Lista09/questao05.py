qtde = 0
digitos = 0

frase = input()
while (not '***' in frase):
	qtde += 1
	for s in frase:
		if (s >= '0' and s <= '9'):
			digitos += 1
	frase = input()

print(qtde)
print(digitos)