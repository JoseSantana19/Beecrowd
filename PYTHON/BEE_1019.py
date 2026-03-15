n = int(input())
tempo = []
for conversao in [3600, 60, 1]:
    tempo.append(n//conversao)
    n = n % conversao
print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")
