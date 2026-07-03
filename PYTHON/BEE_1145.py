x, y = list(map(int, input().split()))
linha = ''
for e in range(1, y+1):
    if e % x != 0:
        linha += f'{e} '
    else:
        linha += f'{e}'
        print(linha)
        linha = ''
