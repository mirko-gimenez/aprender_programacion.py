
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT1973
# Copyright 2023 Ariel H Garcia Traba <cursos.agt@gmail.com> +54 9 11 4475 4637
import os
import time
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione una tecla para continuar")
    print("\n")
'''
https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal

Clasificación   IMC (kg/m²)

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

Algunas organizaciones consideran sobrepeso un índice superior a 27.0.
En adultos (mayores de 18 años) estos valores son independientes de la edad, sea hombre o mujer.

Categoría de nivel de peso  Intervalo del percentil
Bajo peso                   Menos del percentil 5
Eutrófico                   > percentil 5 y < percentil 85
Sobrepeso                   > 85 hasta y < percentil 95
Obeso                       > percentil 95

imitaciones

Correlación entre el IMC y el porcentaje de grasa corporal (%BF) de 8550 hombres en una estadística realizada por el National Health and Nutrition Examination Survey. Los datos en el cuadrante superior izquierdo y en el inferior derecho muestran algunas limitaciones del IMC.9​
El matemático Keith Devlin y el Center for Consumer Freedom (asociación de la industria de la restauración) defiende que el error en el IMC es significante y tan habitual que lo hace inútil para la evaluación de la salud.10​11​ El profesor Eric Oliver de la Universidad de Chicago dijo sin embargo que el IMC era conveniente pero también era una medida del peso inexacto, que fuerza a ciertos grupos de la población y debería ser revisado.12​

Escala
El exponente en el denominador de la fórmula para el IMC es arbitrario. El IMC depende del peso y del «cuadrado» de la altura. Mientras que la masa se incrementa del orden de la tercera potencia, al ser una medida que depende del volumen tridimensional, implica que los individuos más altos con la misma forma de cuerpo y composición relativa tienen un índice mayor de BMI.13​

Ignora variaciones en las características físicas
El IMC añade aproximadamente un 10 % para los individuos más altos y recorta aproximadamente otros 10 % para los más pequeños. En otras palabras, una persona con una talla pequeña podría tener más grasa que el óptimo, pero su BMI reflejar que es «normal». Por el contrario, una persona de talla grande (o alto) podría ser un individuo saludable con un índice de grasa bajo, pero ser clasificado con sobrepeso14​

No diferencia entre masa muscular y masa grasa
El IMC asume una distribución entre la masa muscular y la masa grasa que no son ciertas. El IMC generalmente sobreestima el tejido adiposo en aquellos con mayor masa corporal (por ejemplo atletas) y subestima el exceso de grasa en aquellos con menor masa corporal. Un estudio en junio de 2008 por Romero-Corral examinó a 13 601 sujetos de Estados Unidos y encontró que la obesidad (IMC>30) se encontraba presente en el 21 % de los hombres y el 31 % de las mujeres. Sin embargo, usando el porcentaje de grasa corporal se encontró que la obesidad se encontraba en el 50 % de los hombres y el 62 % de las mujeres. A pesar del subcontaje que estimó el IMC, los valores del IMC sí se encontraban en un rango asociado con porcentajes de grasa corporal grandes.

Variación en la relación con la salud
Un estudio publicado por el Journal of the American Medical Association en 2005 demostró que las personas con sobrepeso tienen una probabilidad de morir similar a las personas con peso normal tal y como lo define el IMC, mientras aquellas «obesas» o «por debajo de lo normal» tienen una probabilidad mayor de morir.15​

Un estudio de 2010 que siguieron a 11 000 sujetos durante 8 años concluyó que el IMC no es una buena medida para considerar el riesgo de ataque al corazón, infarto de miocardio o muerte. Una medida mejor podría ser el índice cintura-altura.16​

Un estudio GWAS publicado en 2015 (realizado en población europea), consiguió identificar loci (Locus) relacionados con el IMC y que ejercían diferentes efectos dependiendo de la edad del grupo de población. Gracias a esto, se pudieron establecer co-relaciones con rasgos cardiometabólicos u obesidad. Sin embargo, aún es necesario investigar más en profundidad estas relaciones con muestras poblacionales más amplias, con el fin de obtener una mejor significación y objetivización de los parámetros.17​

IMC y diabetes
Saber si el índice de masa corporal puede correlacionarse con enfermedades como la diabetes tipo 2, ha despertado gran interés en la comunidad científica. Sin embargo, las investigaciones a la fecha no han confirmado una relación directa entre estos dos parámetros.18​19​

El interés despertó a partir de datos extraídos de dos servicios de medicina en Estados Unidos. La mayoría de los pacientes con índice de masa corporal alto tenían tendencia a trastornos en el metabolismo crónicos como la diabetes. Sin embargo, los resultados obtenidos en las investigaciones no lo confirmaron. Dichos estudios dejan en claro que el IMC no es el mejor método para estimar si una persona puede tener diabetes o no.20​

'''
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
                                            |
Peso bajo                       <18,50      |
     Delgadez severa            <16,00      |
     Delgadez moderada          16,00-16,99 |
     Delgadez leve              17,00-18,49 |
Normal                          18,50-24,99 |
Sobrepeso                       >=25,00     |
     Preobesidad                25,00-29,99 |
     Obesidad                   >=30,00     |
          Obesidad leve         30,00-34,99 |
          Obesidad media        35,00-39,99 |
          Obesidad mórbida      40,00       |''',Style.RESET_ALL)


peso   = 80
altura = 1.75


# ~ import math
# ~ imc = peso / (pow (altura,2))
# ~ imc = peso / (altura *altura)
# ~ imc = peso / (altura **(1/10))
imc =(peso / (altura **2))
print (f"Su imc es de {imc} puntos")
imc =round ( imc, 2)
# ~ print ("Su imc es de",imc,"puntos") #viejo
print (f"Su imc es de {imc} puntos")# nuevo  f-string

#-----------------------------------------------------------------
#                                      primer etapa
#-----------------------------------------------------------------

imc =9
'''
#   mal                               ****solo para ver       
if imc<18.5:
    print ("Peso bajo")
else:
    print ("no tenes peso bajo")
    if imc >= 18.5 and imc <25:
        #Normal                          18,50-24,99
        print ("Peso Normal")
    else:
        print ("Peso no Normal")
        if imc >= 25:
            print ("Sobrepeso")
        #Sobrepeso                       >=25,00
'''
#   mal                               ****solo para ver 
###########################################################################
'''
print ("*"*50)
if imc<18.5:
    print ("Peso bajo")#0 a 18.5     chau
elif imc >= 18.5 and imc <25:
    #Normal                          18,50-24,99
    print ("Peso Normal")
elif imc >= 25:
    print ("Sobrepeso")
    #Sobrepeso                       >=25,00
'''
#  ok
###########################################################################
'''
print ("*"*50)
if imc<18.5:
    print ("Peso bajo")#0 a 18.5     chau
elif imc <25:
    #Normal                          18,50-24,99
    print ("Peso Normal")
else:
    print ("Sobrepeso")
    #Sobrepeso                       >=25,00
print ("fin")
'''
###########################################################################
#-----------------------------------------------------------------
#                                      segunda etapa
#-----------------------------------------------------------------
'''
print ("-"*50)
imc =18.51
print (f"Su imc es de {imc} puntos")
#  ok
print ("*"*50)
if imc<18.5:
    print ("Peso bajo")#0 a 18.5 
    if imc< 16:#0 a 15.9999999999999999
        print ("Delgadez severa")
    elif imc < 17:#elif imc >=16 and imc < 17:
        print ("Delgadez moderada")
    else: #elif imc >=17: y por el if general if imc<18.5:
        print ("Delgadez leve")    # entre >=17 y < 18.5
elif imc <25:
    #Normal                          18,50-24,99
    print ("Peso Normal")
else:
    print ("Sobrepeso")
    #Sobrepeso                       >=25,00
print ("fin")
'''

###########################################################################
'''
#-----------------------------------------------------------------
#                                      trecer etapa
#-----------------------------------------------------------------
print ("-"*50)
imc =26+5
print (f"Su imc es de {imc} puntos")
#  ok
print ("*"*50)
if imc<18.5:
    print ("Peso bajo")#0 a 18.5 
    if imc< 16:#0 a 15.9999999999999999
        print ("Delgadez severa")
    elif imc < 17:#elif imc >=16 and imc < 17:
        print ("Delgadez moderada")
    else: #elif imc >=17: y por el if general if imc<18.5:
        print ("Delgadez leve")    # entre >=17 y < 18.5
elif imc <25:
    #Normal                          18,50-24,99
    print ("Peso Normal")
else:
    print ("Sobrepeso")
    #Sobrepeso                       >=25,00
    if imc < 30:
        print ("Preobesidad")
    else:
        print ("Obesidad")
print ("fin")
'''
###########################################################################
#-----------------------------------------------------------------
#                                      tercer etapa
#-----------------------------------------------------------------
print ("-"*50)
imc =41
print (f"Su imc es de {imc} puntos")
#  ok
print ("*"*50)
if imc<18.5:
    print ("Peso bajo")#0 a 18.5 
    if imc< 16:#0 a 15.9999999999999999
        print ("    Delgadez severa")
    elif imc < 17:#elif imc >=16 and imc < 17:
        print ("    Delgadez moderada")
    else: #elif imc >=17: y por el if general if imc<18.5:
        print ("    Delgadez leve")    # entre >=17 y < 18.5
elif imc <25:
    #Normal                          18,50-24,99
    print ("Peso Normal")
else:
    print ("Sobrepeso")
    #Sobrepeso                       >=25,00
    if imc < 30:
        print ("    Preobesidad")
    else:# IMC >=   30
        print ("    Obesidad")
        if imc < 35: # ~ Obesidad leve         30,00-34,99
            print ("        leve")
        elif imc < 40: #imc >= 35 and imc < 40: # ~ Obesidad media        35,00-39,99
            print ("        media")
        else: # elif imc >= 40: # ~ Obesidad mórbida   >=     40
            print ("        mórbida")

print ("fin")


###########################################################################
#-----------------------------------------------------------------
#                                      tarea
#-----------------------------------------------------------------
print ("-"*50)
print(F'''{Fore.WHITE+Back.BLUE}
                                            |
Sobrepeso                       >=25,00     |
     Obesidad                   >=30,00     |
          Obesidad mórbida      40,00       |
          Obesidad media        35,00-39,99 |
          Obesidad leve         30,00-34,99 |
     Preobesidad                25,00-29,99 |
Normal                          18,50-24,99 |
Peso bajo                       <18,50      |
     Delgadez leve              17,00-18,49 |
     Delgadez moderada          16,00-16,99 |
     Delgadez severa            <16,00      |''',Style.RESET_ALL)












