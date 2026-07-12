impar = []
par = []
for _ in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        if len(par) == 5:
            for i, e in enumerate(par):
                print(f"par[{i}] = {e}")
            par = []
    else:
        impar.append(n)
        if len(impar) == 5:
            for i, e in enumerate(impar):
                print(f"impar[{i}] = {e}")
            impar = []
for i, e in enumerate(impar):
    print(f"impar[{i}] = {e}")
for i, e in enumerate(par):
    print(f"par[{i}] = {e}")
