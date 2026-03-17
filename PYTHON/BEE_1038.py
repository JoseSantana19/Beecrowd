codigo, quantidade = list(map(int, input().split()))
if codigo == 1:
    preco = 4
elif codigo == 2:
    preco = 4.5
elif codigo == 3:
    preco = 5
elif codigo == 4:
    preco = 2
elif codigo == 5:
    preco = 1.5
print(f"Total: R$ {preco*quantidade:.2f}")
