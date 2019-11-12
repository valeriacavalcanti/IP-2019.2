'''
LISTA 05 - QUESTÃO 04 (2.0v)
'''

numeros = []
existe = False
qtde = 0

for i in range(4):
  numeros.append(int(input()))

for i in range(len(numeros)):
  qtde += 1
  if (numeros[i] in numeros[i + 1: 4]):
    existe = True
    break

if (existe == True):
  print('tem repeticao')
else:
  print('nao tem repeticao')

print(qtde)