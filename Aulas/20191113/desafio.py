maior_municipio = ''
maior_valor = 0
municipios = []
populacoes = []
soma = 0

for i in range(223):
	m, p = input().split('-')
	p = int(p)

	municipios.append(m)
	populacoes.append(p)
	
	soma += p
	if (p > maior_valor):
		maior_valor = p
		maior_municipio = m

media = soma/223

print('Municípios que poderão ser afetados:')
for i in range(223):
	if (populacoes[i] <= 5000):
		print(municipios[i], populacoes[i])

print(f'Média = {media}')
print(f'Maior população: {maior_municipio} ({maior_valor})')

print('Municípios que possuem população abaixo da média do Estado:')
for i in range(223):
	if (populacoes[i] < media):
		print(municipios[i], populacoes[i])

