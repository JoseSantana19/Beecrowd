x = int(input())
y = int(input())
if y < x:
    x, y = y, x
soma = 0
for e in range(x, y+1):
    if e % 13 != 0:
        soma += e
print(soma)
