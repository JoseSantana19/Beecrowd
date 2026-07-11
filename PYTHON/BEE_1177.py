t = int(input())
x = 0
for i in range(1000):
    print(f"N[{i}] = {x}")
    if x+1 < t:
        x += 1
    else:
        x = 0
