while True:
    m, n = list(map(int, input().split()))
    
    if m <= 0 or n <= 0:
        break
        
    if m > n:
        m, n = n, m
        
    saida = ''
    soma = 0
    for e in range(m,n+1):
        saida += f"{e} "
        soma += e
    saida += f"Sum={soma}"
    print(saida)
