x = int(input())
while True:
    z = int(input())
    if z > x:
        break
cont, soma = 0, 0
for e in range(x, z):
    soma += e
    cont += 1
    if soma > z:
        break
print(cont)
