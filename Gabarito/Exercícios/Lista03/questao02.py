qtde = 0
soma = 0

idade = int(input('Idade: '))
maior = menor = idade

while (idade != 0):
	qtde += 1
	soma += idade

	if (idade < menor):
		menor = idade
	elif (idade > maior):
		maior = idade

	idade = int(input('Idade: '))

print(f'Quantidade: {qtde}')
if (qtde > 0):
	print(f'Média das idades: {soma/qtde}')
	print(f'Menor idade: {menor}')
	print(f'Maior idade: {maior}')