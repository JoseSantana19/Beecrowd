while True:
    x = int(input())
    if x == 0:
        break
    if x % 2 == 1:
        x += 1
    soma = 0
    for e in range(5):
        soma += x
        x += 2
    print(soma)
