maior = 0
pos_maior = 0

for e in range(100):
    n = int(input())
    if n > maior:
        maior = n
        pos_maior = e + 1
        
print(maior)
print(pos_maior)
