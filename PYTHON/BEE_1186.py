operacao = input()
soma = 0
cont = 0
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if linha + coluna > 11:
            soma += valor
            cont += 1
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{soma/cont:.1f}")
