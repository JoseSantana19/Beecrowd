w1 = int(input().split()[1])
x1, y1, z1 = list(map(int,input().split(" : ")))
w2 = int(input().split()[1])
x2, y2, z2 = list(map(int,input().split(" : ")))

segundos_total = (60 * (1440 * w2 + 60 * x2 + y2) + z2) - (60 * (1440 * w1 + 60 * x1 + y1) + z1)

lista = []
for e in (86400, 3600, 60, 1):
    lista.append(segundos_total // e)
    segundos_total = segundos_total % e

print(f'{lista[0]} dia(s)')
print(f'{lista[1]} hora(s)')
print(f'{lista[2]} minuto(s)')
print(f'{lista[3]} segundo(s)')
