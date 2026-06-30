alcool, gasolina, diesel = 0, 0, 0

while True:
    resp = input()
    if resp == '1':
        alcool += 1
    elif resp == '2':
        gasolina += 1
    elif resp == '3':
        diesel += 1
    elif resp == '4':
        break
    
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
