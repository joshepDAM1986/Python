# #EJERCICIO 5
# Escriba un programa que pida un string y lo muestre al revés
# sin usar bucles.

# palabra=input("Escriba la palabra a revertir ")
# print(f"Su palabra al revés es {palabra[::-1]}")

# EJERCICIO 6
# Escriba un programa que pida un numero y nos diga si es un
# float (mostrar True o False).

# numero = input("Escriba el numero: ")
# print("." in numero and numero.count(".") <= 1)

# EJERCICIO 7
# Escriba un programa que pida un string y cree una variable que
# esté formada por los dos primeros y por los dos últimos
# caracteres. Suponemos que tiene la palabra al menos 4
# caracteres y hay que resolverlo con subcadenas.

# palabra = input("Ingrese una palabra: ")
# nuevaPalabra = palabra[:2] + palabra[-2:]
# print("La nueva variable es:", nuevaPalabra)

# EJERCICIO 8
# Escriba un programa que pida un string y cree una variable que
# esté con el mismo string pero con el primero y último carácter
# caracteres intercambiados. Puede tener cualquier longitud.
# Resolverlo con subcadenas.

palabra = input("Ingrese una palabra o frase: ")
nuevaPalabra = palabra[-1] + palabra[1:-1] + palabra[0]
print("La nueva variable es:", nuevaPalabra)