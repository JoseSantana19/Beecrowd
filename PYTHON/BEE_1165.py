n = int(input())
for _ in range(n):
    x = int(input())
    divisores = 0
    primo = True
    for e in range(1,x+1):
        if x % e == 0:
            divisores += 1
            if divisores > 2:
                primo = False
                break
    if primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
