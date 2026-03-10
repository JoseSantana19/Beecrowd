total = 0
for e in range(2):
    entrada = input().split()
    codigo = int(entrada[0])
    quantidade = int(entrada[1])
    valor = float(entrada[2])
    total += quantidade * valor
print(f"VALOR A PAGAR: R$ {total:.2f}")
