n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    soma = 0
    if x % 2 == 0:
        x += 1
    for e in range(y):
        soma += x
        x += 2
    print(soma)
