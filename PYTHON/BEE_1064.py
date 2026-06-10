contagem = 0
soma = 0
for e in range(6):
    n = float(input())
    if n > 0:
        contagem += 1
        soma += n
print(f"{contagem} valores positivos")
print(f"{soma / contagem :.1f}")
