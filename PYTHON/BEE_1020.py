n = int(input())
idade = []
for conversao in [365, 30, 1]:
    idade.append(n//conversao)
    n = n % conversao
print(f"{idade[0]} ano(s)")
print(f"{idade[1]} mes(es)")
print(f"{idade[2]} dia(s)")
