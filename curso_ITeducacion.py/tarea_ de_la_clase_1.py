"""imc = 4

print(f"su imc es de {imc} puntos")

if imc < 18:
     print("peso bajo")
     if imc < 16:
          print("delgadez severa")
     elif imc < 17:
          print("delgadez moderada")
     else:
          print("delgadez leve")

elif imc <25:
     print("peso normal")

else:
     print("sobre peso")
     if imc < 30:
          print("preobesidad")
     else:
          print ("obesidad")
          if imc < 35:
               print("obesidad leve")
          elif imc < 40:
               print("obesidad media")
          else:
               print("obesidad mordida")       

"""
          
"""imc = 45

if imc > 25:
     print("sobre peso")
     if imc < 29:
          print("pre obesidad")
     elif imc > 30:
          print("obesidad")
          if imc < 34:
               print("obesidad leve")
          elif imc > 35:
               print("obesidad media")
               if imc < 39 :
                    print("")
    
Valores principales Valores adicionales
Peso bajo                       <18,50
     Delgadez severa            <16,00
     Delgadez moderada          16,00-16,99
     Delgadez leve              17,00-18,49
Normal                          18,50-24,99
Sobrepeso                       ≥25,00
     Preobesidad                25,00-29,99
     Obesidad                   ≥30,00
          Obesidad leve         30,00-34,99
          Obesidad media        35,00-39,99
          Obesidad mórbida      40,00               
imc = 11

if imc > 40:
     print("obesidad mordida")
     if imc > 35:
          print("obesidad media")
     elif imc > 30:
          print("obesidad leve")
     else:
          print("sobre peso")
          
if imc > 18:
     print("peso normal")
else :
     print("delgadez leve")

if imc < 16:
     print("delgadez severa")
     if imc < 18:
          print("delgadez modera")
     else:
          print("peso bajo")"""