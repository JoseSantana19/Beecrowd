valor = float(input())

if valor <= 2000:
    imposto = 'Isento'
elif valor <= 3000:
    imposto = f'R$ {0.08 * (valor - 2000) :.2f}'
elif valor <= 4500:
    imposto = f'R$ {0.18 * (valor - 3000) + 80 :.2f}'
else:
    imposto = f'R$ {0.28 * (valor - 4500) + 350 :.2f}'
    
print(imposto)
