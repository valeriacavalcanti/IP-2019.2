h, m, s = input().split(":")
h, m, s = int(h), int(m), int(s)

tempo = h * 3600 + m * 60 + s
sessao = 20 * 3600

print(sessao - tempo)