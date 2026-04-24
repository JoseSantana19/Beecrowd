salario_antigo = float(input())

if salario_antigo <= 400:
    aumento = 15
elif salario_antigo <= 800:
    aumento = 12
elif salario_antigo <= 1200:
    aumento = 10
elif salario_antigo <= 2000:
    aumento = 7
else:
    aumento = 4

novo_salario = salario_antigo * (1 + aumento/100)
reajuste = novo_salario - salario_antigo

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {aumento} %")
