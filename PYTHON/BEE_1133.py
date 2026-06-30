x = int(input())
y = int(input())
if x > y:
    x, y = y, x
for e in range(x+1, y):
    if e % 5 == 2 or e % 5 == 3:
        print(e)
