vetor = []
for _ in range(10):
    vetor.append(int(input()))
for i, e in enumerate(vetor):
    if e <= 0:
        vetor[i] = 1
    print(f"X[{i}] = {vetor[i]}")
