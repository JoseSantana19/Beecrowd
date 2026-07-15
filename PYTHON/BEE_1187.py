operacao = input()
soma = 0
cont = 0
col_min, col_max = 1, 10
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if linha < 5 and col_min <= coluna and col_max >= coluna:
            soma += valor
            cont += 1
    col_min += 1
    col_max -= 1
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{soma/cont:.1f}")
