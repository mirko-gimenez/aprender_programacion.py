#textos:
"string" """string""" '''string''' 'string'
#cadena de texto, no caracter, las comillas simples son para un reglon y las triples para varios.
 
 #numeros
 
 #entero 4. flotate 4.4
numero_float = 1.1

numero_int = 4 
 
 # boolean: true o false. con mayuscula en py.
falso = False

verdadero = True 
 
 #variables: espcaios que se almacena los datos variables en la memoria de nuestro programa.
 #se puede operar dentro de una variable.
 # las var, se declaran y  despues se definen.
nombre = "mirko"
apellido = "gimenez"

# estas cosas que no se su nombre: += ... 10 + 1 ...
caca = 10 + 1

#concatenar:
bienvenida = "hola " + nombre + " ¿como estas?"
print(bienvenida)

#como usar los "f string" que concatena un dato "numero" con los string, si "miNombre" seria un dato numerico nos tira error.
# para que eso no pase usamemos la F, esto lo que hace es que un dato lo convierte a texto, ej.

# la "f-string" permite concatenar un dato de tipo numero con uno de tipo texto.
mi_nombre = 5
mi_apellido = "gimenex"

bienvenidoo = f"holo {mi_nombre} ¿todo bien?"
print(bienvenidoo)

#DEL: elimina la declaracion de una var.

#OPERADORES DE PERTENENCIA:
#print holo in bienvenido: significa que le preguntas si el dato que esta en var y te lo muestra en pantalla con un true y si no esta un false.
#print hola not in bienvenido es todo lo contrario.

print("holo" in bienvenidoo)#true
print("hola" in bienvenidoo)#false
print("holo" not in bienvenidoo)#false
print("hola" not in bienvenidoo)#true

