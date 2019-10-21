qtde = 0

nota = int(input('Informe a nota: '))

while (nota < 0 or nota > 100):
	qtde += 1
	print('Nota inválida. Deve ser entre 0 e 100!')
	nota = int(input('Informe a nota: '))

print(f'Quantidade de notas inválidas: {qtde}')
print(f'Nota válida: {nota}')