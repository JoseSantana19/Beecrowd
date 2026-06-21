n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    if x > y:
        x, y = y, x
    soma = 0
    for e in range(x+1, y):
        if e % 2 == 1:
            soma += e
    print(soma)
