i, j, minimo = 1, 7, 4
while i <= 9:
    print(f"I={i} J={j}")
    j -= 1
    if j == minimo:
        j += 5
        i += 2
        minimo += 2
