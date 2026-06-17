quant_c, quant_r, quant_s = 0, 0, 0
n = int(input())

for _ in range(n):
    q, a = input().split()
    if a == 'C':
        quant_c += int(q)
    elif a == 'R':
        quant_r += int(q)
    elif a == 'S':
        quant_s += int(q)
        
print(f"Total: {quant_c+quant_r+quant_s} cobaias")
print(f"Total de coelhos: {quant_c}")
print(f"Total de ratos: {quant_r}")
print(f"Total de sapos: {quant_s}")
print(f"Percentual de coelhos: {quant_c*100/(quant_c+quant_r+quant_s):.2f} %")
print(f"Percentual de ratos: {quant_r*100/(quant_c+quant_r+quant_s):.2f} %")
print(f"Percentual de sapos: {quant_s*100/(quant_c+quant_r+quant_s):.2f} %")
