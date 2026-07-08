t = int(input())
for _ in range(t):
    entrada = input().split()
    pa, pb = int(entrada[0]), int(entrada[1])
    g1, g2 = float(entrada[2]), float(entrada[3])
    cont = 0
    while pa <= pb:
        pa = (pa*(g1/100+1)) // 1
        pb = (pb*(g2/100+1)) // 1
        cont += 1
    if cont > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{cont} anos.")
