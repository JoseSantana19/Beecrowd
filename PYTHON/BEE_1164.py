n = int(input())
for _ in range(n):
    x = int(input())
    soma_divisores = 0
    for e in range(1,int(x/2)+1):
        if x % e == 0:
            soma_divisores += e
    if soma_divisores == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
