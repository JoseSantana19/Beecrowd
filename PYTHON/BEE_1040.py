n1, n2, n3, n4 = list(map(float, input().split()))
media = (n1*2 + n2*3 + n3*4 + n4) / 10
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    media = (media + exame) / 2
    print(f"Nota do exame: {exame:.1f}")
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
