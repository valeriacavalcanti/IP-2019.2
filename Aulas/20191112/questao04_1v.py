'''
LISTA 05 - QUESTÃO 04 (1.0v)
'''

numeros = []
existe = False
qtde = 0

for i in range(4):
  numeros.append(int(input()))

for i in range(len(numeros)):
  for j in range(i + 1, len(numeros)):
    qtde += 1
    if (numeros[i] == numeros[j]):
      existe = True
      break
  if (existe == True):
    break

if (existe == True):
  print('tem repeticao')
else:
  print('nao tem repeticao')

print(qtde)