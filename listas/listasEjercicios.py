# Ejercicio 16:
# Escribir un programa donde un jugador pueda jugar contra la
# máquina a " piedra"," papel"," tijera"" y spock de
# manera que se seleccione un valor entre " papel",
# tijera"tijera"" y spock por parte del jugador y de manera
# aleatoria usando choice del módulo random

# from random import choice
#
# lista=["piedra","papel","tijera","lagarto","spock"]
# eJugador = str(input("Elije una opción: "))
# if eJugador=="piedra":
#     print(f"El jugador eligió {lista[0]}")
# elif  eJugador=="papel":
#     print(f"El jugador eligió {lista[1]}")
# elif  eJugador=="tijera":
#     print(f"El jugador eligió {lista[2]}")
# elif  eJugador=="lagarto":
#     print(f"El jugador eligió {lista[3]}")
# elif  eJugador=="spock":
#     print(f"El jugador eligió {lista[4]}")
# else:
#     print("Opcion inválida")
#
# eAleatoria = choice(lista)
# print(f"El ordenador eligió {eAleatoria}")


# EJERCICIO 17
# Escribir un programa que dado un texto con mayúsculas y
# minúsculas separado por espacios indique si es o no un
# palíndromo

# palabra=str("Dabale arroz a la zorra el abad")
# lista=palabra.split(" ")
# palabraJunta="".join(lista).lower()
# print(palabraJunta)
# if (palabraJunta[::-1]==palabraJunta):
#     print("Es palindromo")
# else:
#     print("No es palindromo")

# EJERCICIO 18
# Escribir un programa que dado un entero muestre el mismo
# número, pero dado la vuelta

# num=5792
# numStr=str(num)
# numStr=numStr[::-1]
# numStrInvertido="".join(numStr)
# numIntInvertido=int(numStrInvertido)
# print(numIntInvertido)

# EJERCICIO 19
# Escribir un programa que dado un entero muestre el mismo
# número pero con los dígitos ordenados de menor a mayor

num=3285
numStr=str(num)
numStr=sorted(numStr)
numStrOrdenados="".join(numStr)
sumIntOrdenados=int(numStrOrdenados)
print(sumIntOrdenados)