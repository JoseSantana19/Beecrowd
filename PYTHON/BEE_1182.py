c = int(input())
operacao = input()
soma = 0
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if coluna == c:
            soma += valor
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{soma/12:.1f}")
