letra_minuscula = 0
letra_maiuscula = 0
numero = 0
especial = 0

frase = input()

for letra in frase:
	if (letra >= 'a') and (letra <= 'z'):
		letra_minuscula += 1
	elif (letra >= 'A') and (letra <= 'Z'):
		letra_maiuscula += 1
	elif (letra >= '0') and (letra <= '9'):
		numero += 1
	else:
		especial += 1

print(letra_minuscula)
print(letra_maiuscula)
print(numero)
print(especial)