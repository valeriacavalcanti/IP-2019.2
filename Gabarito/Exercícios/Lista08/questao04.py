palavra = input()
qtde = 0

for letra in palavra:
	if (((letra >= 'a') and (letra <= 'z')) or ((letra >= 'A') and (letra <= 'Z'))):
	   qtde += 1

while (qtde < len(palavra)):
	palavra = input()
	qtde = 0
	for letra in palavra:
		if ((letra >= 'a') and (letra <= 'z')) or ((letra >= 'A') and (letra <= 'Z')):
		   qtde += 1

nova_palavra = ''
for letra in palavra:
	if (letra >= 'A') and (letra <= 'Z'):
		nova_palavra += chr(ord(letra) + 32)
	else:
		nova_palavra += letra

palavra = ''
for i in range(len(nova_palavra)):
	if (i % 2 == 0):
		palavra += chr(ord(nova_palavra[i]) - 32)
	else:
		palavra += nova_palavra[i]

print(palavra)