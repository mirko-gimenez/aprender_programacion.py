# si una condicion se cumple(true), generamos el codigo1, si no se cumple(false) la condicion generamos otro codigo2.

edad = 23

pasar = "acceso concedido"

no_pasar = "acceso denegado"

if edad < 18:
    print(no_pasar)
else:
    print(pasar)
    #todo lo que esta dentro de la linea del "if o else" forma parte del controlador.

print(edad) #aca podemos ver como este controlador esta fuera del cuantrante de los controladores condicionales.

# usando el controlador "elif-entonces"

pc= "on"

if pc == "on":
    print("aprender")

elif pc == "off":#"elif" se puede repetir muchas veces.
    print("leer")

else:#crear otra logica mas logica.
    print("me voy a correr") 
    
#ANIDAR "if" 
# los "elif" no pueden ir despues de un "else" por eso los "else" tiene que resonder al "if" anidado.

ingreso_mensual = 3000

gasto_mensual = 2500

if ingreso_mensual == 10000:
    if gasto_mensual <= 2000:
        print("bien")
    else:
        print("no estas bien")

elif ingreso_mensual == 3000:
    print("estas bien en argentina")
    if gasto_mensual > 1000:#Conclusión: Sí, puedes usar if dentro de elif, pero hazlo con cuidado. 
        #Mantén el código legible y simple, y considera refactorizar si la lógica se vuelve demasiado compleja .
        print("gastas mucho")
    
elif ingreso_mensual == 1000:
    print("estas bien en chile")

elif ingreso_mensual == 500:
    print("estas bien en venezuela")
    
else:
    print("sos pobre")   
    
    
#otro ejemplo

ingreso = 1000

gasto = 200000

if ingreso > 1000:
    if gasto - ingreso < 0:
        print("estas en perdida")
    elif gasto - ingreso > 100:
        print("estas bien")
    else:
        print("estas gastando")