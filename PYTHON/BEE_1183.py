soma = 0
qnt = 0
operacao = input()
for linha in range(12):
    for coluna in range(12):
        n = float(input())
        if coluna >= linha + 1:
            soma += n
            qnt += 1
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{soma/qnt:.1f}")
