contagem_notas = []
notas = [100,50,20,10,5,2,1]
n = int(input())
print(n)
while n != 0:
    for nota in notas:
        qnt = n // nota
        n = n % nota
        contagem_notas.append(qnt)
for i, nota in enumerate(notas):
    print(f"{contagem_notas[i]} nota(s) de R$ {nota},00")
