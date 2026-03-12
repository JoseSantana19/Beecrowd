a, b, c = list(map(int, input().split()))
maior = ((a + b + abs(a - b)) / 2)
maior = ((maior + c + abs(maior - c)) / 2)
print(f'{int(maior)} eh o maior')
