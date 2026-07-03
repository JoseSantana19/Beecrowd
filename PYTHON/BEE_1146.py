while True:
    x = int(input())
    if x == 0:
        break
    linha = ''
    for e in range(1,x+1):
        if e != x:
            linha += f"{e} "
        else:
            linha += f"{e}"
    print(linha)
