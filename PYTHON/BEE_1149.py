entrada = list(map(int, input().split()))
a, n = entrada[0], entrada[-1]
soma = 0
for i in range(n):
    soma += a + i
print(soma)
