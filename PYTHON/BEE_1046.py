inicio, fim = list(map(int, input().split()))
if fim > inicio:
    tempo = fim - inicio
else:
    tempo = fim + 24 - inicio
print(f"O JOGO DUROU {tempo} HORA(S)")
