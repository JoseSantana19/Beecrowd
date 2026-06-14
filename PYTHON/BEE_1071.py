x = int(input())
y = int(input())

if x < y:
    y, x = x, y

soma = 0
for e in range(y+1, x):
    if e % 2 == 1:
        soma += e
        
print(soma)
