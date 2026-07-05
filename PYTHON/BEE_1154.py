cont, soma = 0, 0
while True:
    n = int(input())
    if n < 0:
        break
    soma += n
    cont += 1
print(f"{soma/cont:.2f}")
