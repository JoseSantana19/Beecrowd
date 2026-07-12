n = int(input())
lista = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        menor = lista[i]
        posicao = 0
    else:
        if lista[i] < menor:
            menor = lista[i]
            posicao = i
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
