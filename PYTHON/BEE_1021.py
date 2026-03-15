n = float(input())
n = int(n * 100)

dinheiro = [10000,5000,2000,1000,500,200,100,50,25,10,5,1]

for valor in dinheiro:
    
    if valor == 10000:
        print("NOTAS:")
    elif valor == 100:
        print("MOEDAS:")
    
    qnt = n // valor
    n = n % valor
    
    if valor >= 200:
        print(f"{qnt} nota(s) de R$ {valor/100:.2f}")
    else:
        print(f"{qnt} moeda(s) de R$ {valor/100:.2f}")
