soma = 0
qtde_10_20 = 0
qtde_0 = 0

desc, valor = input().split()
valor = float(valor)
soma += valor
if (valor >= 10) and (valor <= 20):
	qtde_10_20 += 1
if (valor == 0):
	qtde_0 += 1

menor = valor

for i in range(10):
	desc, valor = input().split()
	valor = float(valor)
	soma += valor
	if (valor >= 10) and (valor <= 20):
		qtde_10_20 += 1
	if (valor == 0):
		qtde_0 += 1
	if (valor < menor):
		menor = valor

print(soma)
print(menor)
print(qtde_10_20)
print(qtde_0)
print(soma/4)