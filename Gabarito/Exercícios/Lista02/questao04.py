n1 = 0
n2 = 1

qtde = int(input('Quantidade: '))

for i in range(qtde):
	print(n1, '', end='')
	n1, n2 = n2, n1
	n2 = n1 + n2

print()