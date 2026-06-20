i, j = 1, 7
while i <= 9:
    print(f"I={i} J={j}")
    j -= 1
    if j == 4:
        j = 7
        i += 2
