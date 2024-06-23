#son datos que dentro tienen otros datos, simples o compuestos pero que podemos agruparlos
# a continuacion una lista: conjunto de datos.}

lista = [" soy mirko ", " de apellido gimenez ", True, 1.79]
#esto sirve para agrupar datos .
print(lista)
#dame el elemento numero 1.
print(lista[1])
#tener en cuenta que se cuanta siempre desde cero, 0...
# el tipo de dato TUPLA no se puede modificar. y el tipo de dato LISTA, si.

lista[2] = False #modifique el dato del elemento 3
print (lista [2])
tupla = (" soy mirko ", " de apellido gimenez ", True, 1.79)
print(tupla)
print(tupla[2])
#todo para mostrar el dato va con [].
#esto funciona para que el dato nunca cambie.

#EL CONJUNTO O SET.
# para crearlo usamos {}.
conjunto = {" soy mirko ", " de apellido gimenez ", True, 1.79,"esto es del conjunto"}
print(conjunto)
# no tienen orden numerico, son elementos desordenados que pueden cambiar, en un conjunto no puede haber datos duplicados, para hacer a lo datos se usa un bucle 
# creando un diccionario(dict).

diccionario = {
    'nombre' : "mirko",
    #clave : valor. asi es en el termino de programacion.
    'apellido' : "gimenez",
    'edad' : 23,
    'masculino' : True,
    'dato_duplicado' : "mirko"
    #es igual que las listas solo que aca se busca el ELEMENTO por su nombre
    # esto tampoco tiene un orden.
}
print(diccionario["masculino"])
# un ejemplo de como puedo sumar algo .
print(diccionario['edad'] - 1)

