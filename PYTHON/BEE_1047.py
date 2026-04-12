hora_inicio, minutos_inicio, hora_fim, minutos_fim = list(map(int, input().split()))

tempo_inicio = hora_inicio * 60 + minutos_inicio
tempo_fim = hora_fim * 60 + minutos_fim
tempo_dia = 24 * 60

if tempo_fim > tempo_inicio:
    tempo_total = tempo_fim - tempo_inicio
elif tempo_fim < tempo_inicio:
    tempo_total = (tempo_fim + tempo_dia) - tempo_inicio
else:
    tempo_total = tempo_dia
    
horas_total = tempo_total // 60
minutos_total = tempo_total % 60

print(f'O JOGO DUROU {horas_total} HORA(S) E {minutos_total} MINUTO(S)')
