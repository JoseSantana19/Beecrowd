lista_total = [0,0,0]
lista_acertos = [0,0,0]
n = int(input())
for e in range(n):
    nome = input()
    s_total, b_total, a_total = list(map(int, input().split()))
    s_certos, b_certos, a_certos = list(map(int, input().split()))
    lista_total[0] += s_total
    lista_total[1] += b_total
    lista_total[2] += a_total
    lista_acertos[0] += s_certos
    lista_acertos[1] += b_certos
    lista_acertos[2] += a_certos
print(f"Pontos de Saque: {lista_acertos[0]*100/lista_total[0]:.2f} %.")
print(f"Pontos de Bloqueio: {lista_acertos[1]*100/lista_total[1]:.2f} %.")
print(f"Pontos de Ataque: {lista_acertos[2]*100/lista_total[2]:.2f} %.")
