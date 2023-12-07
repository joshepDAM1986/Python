# EJERCICIO 2
# Pedir un número de dados (si es negativo salir del programa con un mensaje de error) y tire esa cantidad de dados para dos jugadores (jugador A y jugador B). El jugador que saque más puntos sumando su valor más alto y su valor más bajo, gana.
# b)	(0,5 Puntos). Pedir el tamaño de una contraseña (comprobar que no sea negativo) que generará el programa usando los siguientes caracteres: @$_ABCDEFRSTUVXYZghijklmnpq


from random import randint
from random import choice

numDados = int(input("Introduce el numero de dados: "))
jugadorA = []
jugadorB = []
if numDados < 0:
    print("El numero debe ser positivo")
else:
    if numDados > 0:
        for _ in range(numDados):
            random1 = randint(1, 6)
            random2 = randint(1, 6)
            jugadorA.append(random1)
            jugadorB.append(random2)

        sumaJA = min(jugadorA) + max(jugadorA)
        sumaJB = min(jugadorB) + max(jugadorB)

        if sumaJA == sumaJB:
            print("Empate")
        elif sumaJA > sumaJB:
            print("Jugador A")
        else:
            print("Jugador B")
    else:
        print("Empate")

caracteres = "@$_ABCDEFRSTUVXYZghijklmnpq"
numLon = int(input("Que longitud quieres que tenga la contraseña: "))
if numLon < 0:
    print("El numero debe ser positivo")
else:
    pasword = ""
    for _ in range(numLon):
        pasword += choice(caracteres)
    print(pasword)
