piscadas = 0
soma = 0
while piscadas < 3:
    entrada = input()
    if entrada == 'caw caw':
        print(soma)
        soma = 0
        piscadas += 1
    else:
        if entrada[0] == '*':
            soma += 4
        if entrada[1] == '*':
            soma += 2
        if entrada[2] == '*':
            soma += 1
