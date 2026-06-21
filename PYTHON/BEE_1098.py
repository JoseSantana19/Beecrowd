i, j, cont = 0, 1, 0
while i <= 2:
    cont += 1
    if i % 1 >= 0.99 or i % 1 == 0:
        print(f"I={i:.0f} J={j:.0f}")
    else:
        print(f"I={i:.1f} J={j:.1f}")
    if cont == 3:
        i += 0.2
        j -= 1.8
        cont = 0
    else:
        j += 1
