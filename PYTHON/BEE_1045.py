a, b, c = sorted(list(map(float, input().split())), reverse=True)
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if len(set([a,b,c])) == 1:
        print("TRIANGULO EQUILATERO")
    elif len(set([a,b,c])) == 2:
        print("TRIANGULO ISOSCELES")
