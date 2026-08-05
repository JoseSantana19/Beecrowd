op = input()
soma, cont = 0, 0
for linha in range(12):
    for coluna in range(12):
        n = float(input())
        if linha + coluna <= 10 and linha > coluna:
            soma += n
            cont += 1
if op == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/cont:.1f}')
