# EJERCICIO 20
# Escriba un programa que a partir de dos listas genera listas
# con los siguientes contenidos

# • Palabras que aparecen en las dos listas
# • Palabras que están en la primera, pero no en la segunda
# • Palabras que aparecen en la segunda, pero no en la primera
# • Palabras que aparecen en ambas listas

lista1=["gato","perro","gusano","araña","pajaro"]
lista2=["gato","insecto","pajaro","lagarto","escorpion"]


# • Palabras que aparecen en las dos listas
pRepetidas=[]
for i in lista1:
    if i in lista2:
        pRepetidas.append(i)
print("Palabras que aparecen en las dos listas:", pRepetidas)

# • Palabras que están en la primera, pero no en la segunda
exLista1=[]
for i in lista1:
    if i not in lista2:
         exLista1.append(i)
print("Palabras exclusivas de lista1:", exLista1)

# • Palabras que aparecen en la segunda, pero no en la primera
exLista2=[]
for i in lista2:
    if i not in lista1:
        exLista2.append(i)
print("Palabras exclusivas de lista2:", exLista2)

# • Palabras que aparecen en ambas listas
lConbinada=[]
for i in lista1 + lista2:
    if i not in lConbinada:
        lConbinada.append(i)
print("Listas combinadas:", lConbinada)

# EJERCICIO 21
# Escribir un programa que dada una lista elimine sus valores
# repetidos

lista = ["Jose", "Enrique", "Ruben", "David", "Fabio", "Jose"]
listaNoRep = []

for i in lista:
    if i not in listaNoRep:
        listaNoRep.append(i)

print("Lista sin repetir:", listaNoRep)

# Lo mismo pero sin crear una lista nueva
for i in lista:
    if lista.count(i) > 1: # cuenta si hay algun elemento que aparezca mas de una vez
       lista.remove(i) # elimina los elementos repetidos dejando solo uno de cada en la lista

print("Lista sin repetir:", lista)


# EJERCICIO 22 Escriba un programa que dado un texto nos diga
# cuantas vocales en total hay en dicho texto

texto="multiplataforma"
lista=["a","e","i","o","u"]
contador=0

for i in texto:
    if i.lower() in lista:
        contador+=1
print(f"El número de vocales de {texto}: {contador}")


# EJERCICIO 23
# Escriba un programa que dado un texto nos muestre el numero de
# apariciones de cada una de las 5 vocales

texto="multiplataforma"
contador=[0,0,0,0,0]
vocales=["a","e","i","o","u"]

for i in texto:
    if i == vocales[0]:
        contador[0] += 1
    elif i == vocales[1]:
        contador[1] += 1
    elif i == vocales[2]:
        contador[2] += 1
    elif i == vocales[3]:
        contador[3] += 1
    elif i == vocales[4]:
        contador[4] += 1

for i in range(len(vocales)):
    print(f"Número de apariciones de la vocal {vocales[i]}: {contador[i]}")