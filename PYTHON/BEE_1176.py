t = int(input())
for _ in range(t):
    n = int(input())
    fb1 = 0
    fb2 = 1
    cont = 0
    while cont < n:
        temp = fb1
        fb1 = fb2
        fb2 = temp + fb1
        cont += 1
    print(f"Fib({n}) = {fb1}")
