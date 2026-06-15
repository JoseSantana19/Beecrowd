n = int(input())
for _ in range(n):
    a, b, c = list(map(float, input().split()))
    media = (a*2 + b*3 + c*5) / 10
    print(f"{media:.1f}")
