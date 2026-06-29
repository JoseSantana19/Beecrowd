vit_inter, vit_gremio, empate = 0, 0, 0
while True:
    gols_inter, gols_gremio = list(map(int, input().split()))
    
    if gols_inter > gols_gremio:
        vit_inter += 1
    elif gols_inter < gols_gremio:
        vit_gremio += 1
    else:
        empate += 1
        
    print("Novo grenal (1-sim 2-nao)")
    resp = input()
    if resp == '2':
        break
        
print(f"{vit_inter + vit_gremio + empate} grenais")
print(f"Inter:{vit_inter}")
print(f"Gremio:{vit_gremio}")   
print(f"Empates:{empate}")

if vit_inter > vit_gremio:
    print("Inter venceu mais")
elif vit_inter < vit_gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
