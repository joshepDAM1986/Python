# numeros = [1,2,3,4]
#
# print (numeros [0]) #primero
# print (numeros [-1]) #Ultimo
#
# detodounpoco=[3.5,"Todo",True,4]
# print(detodounpoco[1:3])
# print(detodounpoco[2:])
#
# personas=[["Pepe",34],["Antonio",43],["Maria",56]]
#
# print(personas[0])
# print(personas[1][1])

# cosas = ["Atún", [3.5], [True, 9.8], ["noooo", 23], False]
#
# print(cosas[1])        # Imprime la segunda elemento de la lista cosas, que es [3.5]
# print(cosas[1][0])      # Imprime el primer elemento de la segunda lista, que es 3.5
# #print(cosas[2][2][0])   # Imprime el primer elemento de la tercera lista interna, que es True
# print(cosas[3])         # Imprime el cuarto elemento de la lista cosas, que es ["noooo", 23]
#
# coleccion= ["Jaime","Gabriel","CIDEP","Manantia"]
# #copia=coleccion
# copia=list(coleccion)
#
# copia[1]="David"
# print(coleccion)
# print(copia)
#
# tupla=(1,2,3,4,[5,6])
# #tupla[0]=6 #las tuplas no se puede modificar
# tupla[-1][0]=90 #puedes modificar una lista dentro de una tupla
# print(tupla)

# notas=[7.5,3,8,8,9,5,10,4.5,10,6.7]
# print(notas.index(3))# index imprime la posicion de la nota elegida
# #print(notas.index(15))# no existe esa nota en el array. Error
# print(notas.count(8))# count imprime el numero de veces que encuentra la nota
# print(max(notas))# max imprime la mayor nota del array
# print(min(notas))# min imprime la menor nota del array

# frase="Este no es el año de David"
# partes=frase.split(" ")
# print(partes)
#
# lista=["P","Y","T","H","O","N"]
#
# palabra=":".join(lista)
# print(palabra)
# union="-"
# palabra=union.join(lista)
# print(palabra)

cosas=["balon","futbol","balon"]
cosas.insert(0,"jugador")# insert coloca el elemento en la posicion indicada desplazando el anterior a la derecha
print(cosas)

numeros=[7,8,1,4,2,6,9]
numeros.sort() #ordena de menor a mayor
print(numeros)
numeros.sort(reverse=True) #ordena de mayor a menor
print((numeros))

palabras=["porteria","balon","melon"]
palabras.sort() #si son string ordena alfabeticamente
print(palabras)
