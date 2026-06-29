while True:
    soma = 0
    cont = 0
    while cont < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            cont += 1
            soma += nota
        else:
            print("nota invalida")
    media = soma / 2
    print(f"media = {media:.2f}")
    while True:
        print("novo calculo (1-sim 2-nao)")
        resp = input()
        if resp in ('1','2'):
            break
    if resp == '2':
        break
