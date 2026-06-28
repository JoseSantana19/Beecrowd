cont = 0
soma = 0
while cont < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        cont += 1
        soma += nota
    else:
        print("nota invalida")
media = soma / 2
print(f"media = {media:.2f}")
