senha = input()
qtde = 0

for letra in senha:
	if (letra >= '0') and (letra <= '9'):
		qtde += 1

while (qtde < len(senha)):
	senha = input()
	qtde = 0
	for letra in senha:
		if (letra >= '0') and (letra <= '9'):
			qtde += 1

print(senha)