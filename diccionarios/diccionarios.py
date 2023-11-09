# vocales={
# #clave  #valor
#     "a":0,
#     "e":0,
#     "i":0,
#     "o":0,
#     "u":0
# }
#
# numVocales=0
#
# texto="Hola muy buenas tardes me llamo Juanito"
#
# for letra in texto:
#     if letra.lower() in numVocales:
#         numVocales[letra.lower()]+=1
#         print(f"El numero de vocales del texto {texto} es:")
#
# print(vocales["a"])
# vocales["a"]+=1
# print(vocales["a"])
# print(vocales.get("z","no existe esa vocal"))
#
# tienda={
#     #clave   #valor
#     "patata":1.89,
#     "sandia":2.5,
#     "lechuga":0.80,
#     "cocacola":1.10
# }
#
# print(tienda.get("melon","no existe ese producto"))
# tienda["melon"]=3.2
# print(f"Melon precio {tienda.get('melon','no existe ese producto')}")
#
# print("melon"in tienda) #true
# print("melones"in tienda) #false
#
# #clonar diccionario de tienda
# copia_tienda=dict(tienda)
#
# ofertas=[["jamon",45],["melocotones",2.3]]
# ofertas_dic=dict(ofertas)
# ofertas_dic=dict([["jamon",45],["melocotones",2.3]])
# print(ofertas_dic)
#
# nombres=["jose","jaime","manuel"]
# notas=[8,5,6]
#
# expedientes=dict(zip(nombres,notas))
# print(expedientes)
#
# print(max(tienda)) # busca sobre las claves no sobre el valor
# print(max(tienda, key=tienda.get)) # busca sobre el valor
# print(min(tienda)) # busca sobre las claves no sobre el valor
# print(min(tienda, key=tienda.get)) # busca sobre el valor
#
# print(sorted(tienda)) # busca sobre las claves no sobre el valor
# print(sorted(tienda, key=tienda.get)) # busca sobre el valor
# print(sorted(tienda, key=tienda.get,reverse=True)) # busca sobre el valor invierte


tienda={
    #clave   #valor
    "patata":1.89,
    "sandia":2.5,
    "lechuga":0.80,
    "cocacola":1.10
}

for dato in tienda: #Imprime la clave
    print(dato,end=" ")
print("Adios")

for dato in tienda.keys(): #Imprime la clave
    print(dato,end=" ")
print("Las claves")

for dato in tienda.values(): #Imprime los valores
    print(dato,end=" ")
print("Los valores")
print()

# Aunque funciona, no es muy eficiente
for clave in tienda.keys():
    print(f"{clave} vale {tienda[clave]} €/Kg")
print()

# Es más eficiente, recomendado
for entrada in tienda.items():
    print(f"{entrada[0]} vale {entrada[1]} €/Kg")
print()

for (clave,valor) in tienda.items():
    print(f"{clave} vale {valor} €/Kg")

print(tienda.items()) #devuelve una lista de tuplas