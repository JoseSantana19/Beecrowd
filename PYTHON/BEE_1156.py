y = 1
soma = 0
for x in range(1,40,2):
    soma += x/y
    y *= 2
print(f"{soma:.2f}")
