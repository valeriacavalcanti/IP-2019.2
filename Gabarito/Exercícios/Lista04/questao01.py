tempo = int(input("Tempo: "))

hora = tempo // 3600
minuto = tempo % 3600 // 60
segundos = tempo % 60

print(f"{hora}:{minuto}:{segundos}")