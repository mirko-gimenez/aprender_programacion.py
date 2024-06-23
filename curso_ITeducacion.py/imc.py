imc = 30 

print(f"su imc es de {imc} puntos")

if imc < 18.5:#si es menos a 18 entra en peso bajo.
    print("peso bajo")
    if imc < 16:# si es peso bajo entra en delgadez.
        print("     delgadez severa")
    elif imc < 17:
        print("     delgadez moderada")
    else:
        print("     delgadez leve")
elif imc < 25:# si es menor a 25 entra en peso bajo.
    print("peso normal")
else:#sino entra en sobre peso.
    print("sobre peso")
    if imc < 30:
        print("     pre obesidad")
    else:
        print("     obesidad")
        if imc < 35:
            print("         leve")
        elif imc < 40:
            print("     moderada")
        else:
            print("     severa")