n = int(input())
fib = [0,1]
for e in range(n-2):
    fib.append(fib[-1] + fib[-2])
print(" ".join(map(str, fib)))
