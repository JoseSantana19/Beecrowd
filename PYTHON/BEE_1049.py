corpo = input()
grupo = input()
alimentacao = input()

if corpo == 'vertebrado':
    if grupo == 'ave':
        if alimentacao == 'carnivoro':
            resp = 'aguia'
        elif alimentacao == 'onivoro':
            resp = 'pomba'
    elif grupo == 'mamifero':
        if alimentacao == 'herbivoro':
            resp = 'vaca'
        elif alimentacao == 'onivoro':
            resp = 'homem'
elif corpo == 'invertebrado':
    if grupo == 'inseto':
        if alimentacao == 'hematofago':
            resp = 'pulga'
        elif alimentacao == 'herbivoro':
            resp = 'lagarta'
    elif grupo == 'anelideo':
        if alimentacao == 'hematofago':
            resp = 'sanguessuga'
        elif alimentacao == 'onivoro':
            resp = 'minhoca'
            
print(resp)
