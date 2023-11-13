# EJERCICIO 5
# Escribir un programa que, partiendo de una estructura de datos con los precios de las frutas de una tienda, permita realizar las siguientes acciones:
# Fruta Precio/Kg
# Plátano 1.35
# Manzana 1.80
# Pera 0.85
# Naranja 0.70
#  Dado un número de kilos X mostrar el precio total de llevarse X kilos de todas las frutas. Hacer un resumen de cada
#  cantidad de dinero por fruta y mostrar el total al final.
#  Mostrar la fruta con menor precio por kilo.
#  Crear otro diccionario a partir del anterior con las frutas ordenadas de mayor a menor precio.
#  Crear otro diccionario a partir del anterior con solo las frutas que valgan más de 1€/kg.


# Dado un número de kilos X mostrar el precio total de llevarse X kilos de todas las frutas. Hacer un resumen de cada
#  cantidad de dinero por fruta y mostrar el total al final.

frutas= {
    "Platano":1.35,
    "Manzana":1.80,
    "Pera":0.85,
    "Naranja":0.7
}

fruta=""
precio=0.0
precioTotal=0.0

kilos=int(input("Ingrese el número de kilos: "))

for elemento, valor  in frutas.items():
    precio=round(valor*kilos,2)
    precioTotal+=precio
    fruta=elemento
    print(f"{fruta}: {precio}")
print(f"Precio Total= {precioTotal}")
print()

#  Mostrar la fruta con menor precio por kilo.

fruta=""
precio=0.0

for elemento, valor in frutas.items():
    if precio < valor:
        precio=valor
        fruta=elemento
print(fruta,":",precio)
print()

#  Crear otro diccionario a partir del anterior con las frutas ordenadas de mayor a menor precio.

print(max(frutas))

frutasOrdenadas = {fruta:precio for fruta, precio in sorted(frutas.items())}
print(frutasOrdenadas)

frutasOrdInverted= dict(sorted(frutasOrdenadas.items(), reverse=True))
print(frutasOrdInverted)
print()

#  Crear otro diccionario a partir del anterior con solo las frutas que valgan más de 1€/kg.
frutasOrdenadas = {fruta:precio for fruta, precio in sorted(frutas.items()) if precio > 1}
print(frutasOrdenadas)